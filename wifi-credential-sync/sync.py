import datetime
import os
import logging
import collections

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import *

import requests
from requests.auth import HTTPBasicAuth

from config import *

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG)
logging.info('Starting sync')

logging.debug('Connecting to database')
e = create_engine("mysql://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_NAME))
e.connect()

logging.debug('Constructing session')
s = Session(bind=e)

logging.debug('Querying Bloom Memberships API')
r = requests.get('https://{}/api/users'.format(HOST), headers={'Authorization': 'Token {}'.format(TOKEN)})

if r.status_code != 200:
	logging.error('API query caused status code {} instead of expected 200'.format(r.status_code))


counters = collections.defaultdict(int)

logging.debug('Beginning iteration')
for data in r.json()['users']:
	username = data['wifi_username']

	if s.query(UserInfo).filter(UserInfo.username == username, UserInfo.creationby != 'memberships-sync').count():
		logging.warning('Skipped {}, as existing unmanaged user with same name'.format(username))
		continue

	u = s.query(UserInfo).filter_by(username=username, creationby='memberships-sync').first()

	# If pre-existing user who is enabled, we update their details
	if u and data['wifi_access?']:
		pw = s.query(RADCheck).filter_by(username=username, attribute='Cleartext-Password').first()

		# If data has actually changed, we update the database
		if u.firstname != data['firstname'] or u.lastname != data['lastname'] or pw.value != data['wifi_password']:
			u.firstname = data['firstname']
			u.lastname = data['lastname']

			u.updatedate = datetime.datetime.now()
			u.updateby = 'memberships-sync'

			pw.value = data['wifi_password']

			s.commit()

			logging.debug('Updated {}'.format(username))
			counters['updated'] += 1
		else:
			logging.debug('Skipped {} as is unchanged'.format(username))
			counters['skipped_unchanged'] += 1

	# If pre-existing user who is disabled, we delete their UserInfo and password
	elif u and not data['wifi_access?']:
		for rc in u.radchecks:
			s.delete(rc)
		s.delete(u)

		logging.debug('Deleted {}'.format(username))
		counters['deleted'] += 1

	# If new user who is enabled and has set their wifi password, we create their account
	elif not u and data['wifi_access?'] and data['wifi_password']:
		u = UserInfo()
		u.username = data['wifi_username']
		u.firstname = data['firstname']
		u.lastname = data['lastname']
		u.email = data['wifi_username']

		u.creationdate = datetime.datetime.now()
		u.creationby = 'memberships-sync'

		rc = RADCheck()
		rc.user = u
		rc.attribute = 'Cleartext-Password'
		rc.op = ':='
		rc.value = data['wifi_password']

		s.add(u)
		s.add(rc)
		s.commit()

		logging.debug('Created {}'.format(username))
		counters['created'] += 1

	else:
		logging.debug('Skipped {} as is inactive/disabled'.format(username))
		counters['skipped_inactive'] += 1

logging.info('Stats: ' + ', '.join('{}: {}'.format(t, c) for t, c in counters.items()))
logging.info('Sync completed')
