import datetime
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import *

import requests
from requests.auth import HTTPBasicAuth

TOKEN = os.environ['BLOOM_API_TOKEN']
HOST = os.environ['BLOOM_API_HOST']
DB_USER = os.environ['RADIUS_DB_USER']
DB_PASS = os.environ['RADIUS_DB_PASS']
DB_NAME = os.environ['RADIUS_DB_NAME']
DB_HOST = os.environ['RADIUS_DB_HOST']

e = create_engine("mysql://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_NAME))
s = Session(bind=e)

r = requests.get('https://{}/api/users'.format(HOST), headers={'Authorization': 'Token {}'.format(TOKEN)})

if r.status_code != 200:
	exit('Panic!')

for data in r.json()['users']:
	username = data['wifi_username']

	if s.query(UserInfo).filter(UserInfo.username == username, UserInfo.creationby != 'memberships-sync').count():
		print('WARNING: Skipped {}, as existing unmanaged user with same name'.format(username))
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

			print('Updated {}'.format(username))
		else:
			print('Skipped {} as is unchanged'.format(username))

	# If pre-existing user who is disabled, we delete their UserInfo and password
	elif u and not data['wifi_access?']:
		for rc in u.radchecks:
			s.delete(rc)
		s.delete(u)

		print('Deleted {}'.format(username))

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

		print('Created {}'.format(username))

	else:
		print('Skipped {} as is inactive/disabled'.format(username))

