import datetime
import os
import logging
import json

# Fix for SNI problems on older Python versions
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

from unifi.controller import Controller

import requests
from requests.auth import HTTPBasicAuth

from config import *
c = Controller(CONTROLLER_IP, CONTROLLER_USERNAME, CONTROLLER_PASSWORD, CONTROLLER_PORT, CONTROLLER_VERSION, CONTROLLER_SITEID)

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.INFO)
logging.info('Starting sync')

logging.debug('Fetching users')
users = [[x['_id'], x['name'], x['x_password']] for x in c.get_radius_users()]
user_name_mapping = {}

logging.debug('Querying Bloom Memberships API')
r = requests.get('https://{}/api/users'.format(HOST), headers={'Authorization': 'Token {}'.format(TOKEN)})

if r.status_code != 200:
	logging.error('API query caused status code {} instead of expected 200'.format(r.status_code))

counters = {v : 0 for v in ['updated', 'skipped_unchanged', 'skipped_inactive', 'deleted', 'created']}

logging.debug('Beginning iteration')
for data in r.json()['users']:
	username = data['wifi_username']

	u = None
	for user in users:
		if user[1] == username:
			u = user 
			break

	# If pre-existing user who is enabled, we update their details
	if u and data['wifi_access?']:
		users.remove(u)
		pw = u[2]
		user_name_mapping[u[0]] = {'firstname': data['firstname'], 'lastname': data['lastname']}
		# If data has actually changed, we update the database
		if pw != data['wifi_password']:
			try:
				c.put_radius_user(u[0], u[1], data['wifi_password'])
			except:
				logging.error('API query error updating wifi password of {} {}'.format(u[1], u[0]))

			logging.info('Updated {}'.format(username))
			counters['updated'] += 1
		else:
			logging.debug('Skipped {} as is unchanged'.format(username))
			counters['skipped_unchanged'] += 1

	# If pre-existing user who is disabled, we delete their UserInfo and password
	elif u and not data['wifi_access?']:
		users.remove(u)
		try:
			c.delete_radius_user(u[0])
		except:
			logging.error('API error deleting radius user {}'.format(u[0]))

		logging.info('Deleted {}'.format(username))
		counters['deleted'] += 1

	# If new user who is enabled and has set their wifi password, we create their account
	elif not u and data['wifi_access?'] and data['wifi_password']:
		try:
			c.add_radius_user(data['wifi_username'], data['wifi_password'])
		except:
			logging.error('API error adding radius user {}'.format(data['wifi_username']))
		user_name_mapping[data['wifi_username']] = {'firstname': data['firstname'], 'lastname': data['lastname']}

		logging.info('Created {}'.format(username))
		counters['created'] += 1

	else:
		logging.debug('Skipped {} as is inactive/disabled'.format(username))
		counters['skipped_inactive'] += 1

for user in users:
	if user[0]:
		try:
			c.delete_radius_user(user[0])
			logging.info('Deleted {}'.format(user[1]))
			counters['deleted'] += 1
		except:
			logging.error('Error deleting outdated wifi user {}'.format(user[1]))

with open('user_mapping.json', 'w') as out:
	out.write(json.dumps(user_name_mapping))
logging.info('Stats: ' + ', '.join('{}: {}'.format(t, c) for t, c in counters.items()))
logging.info('Sync completed')
