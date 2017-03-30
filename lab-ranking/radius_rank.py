#!/usr/bin/env python3
# Parses freeradius authentication logs to generate stats about presence in lab
# Configure in crontab to write to http://<website>/ranking.json to be read by bubble-rank.html
# Using Python 3.3+
import gzip, glob, datetime, re, itertools, json, subprocess

CUR_DIR = "/root/infrastructure-automation/lab-ranking/radiuslogs/"
logex = re.compile("^(.*?) : Auth: Login OK: \[(.*?)\] .*?$")

uname_map = {}
subprocess.call(["/root/infrastructure-automation/lab-ranking/radius_log_copy.sh"])
with open('/root/infrastructure-automation/wifi-credential-sync/user_mapping.json') as input:
	uname_map = json.loads(input.read())
	for username in uname_map:
		firstname = uname_map[username]['firstname']
		lastname = uname_map[username]['lastname']
		if firstname or lastname:
			if firstname and lastname:
				uname_map[username]['name'] = firstname + " " + lastname
			elif firstname:
				uname_map[username]['name'] = firstname
			elif lastname:
				uname_map[username]['name'] = lastname

logs = [open(CUR_DIR + "radius.log", encoding="UTF-8", errors="ignore")]

entries = []

for path in glob.iglob(CUR_DIR + "radius.log.[0-9].gz"):
	logs.append(gzip.open(path, 'rt', encoding="UTF-8", errors="ignore"))

for path in glob.iglob(CUR_DIR + "radius.log.[0-9]"):
	logs.append(open(path, 'r', encoding="UTF-8", errors="ignore"))

for flog in logs:
	for line in flog:
		match = logex.match(line)		
		if match:
			time = datetime.datetime.strptime(match.group(1), "%a %b %d %H:%M:%S %Y") # Sun Jun 14 03:38:36 2015
			user = match.group(2).lower()
			entries.append((time, user))


dates_users = []

entries.sort(key=lambda x: x[0])
for date, records in itertools.groupby(entries, lambda x: datetime.date(x[0].year, x[0].month, x[0].day)):
	users = set()
	for ts, user in records:
		users.add(user.lower().strip())
	dates_users.append((date, users))

rolling_count = {}
for date, users in dates_users[-30:]:
	for user in users:
		if user not in rolling_count.keys():
			rolling_count[user] = 0

		rolling_count[user] += 1

output = []
for username, days in rolling_count.items():
	record = {}
	record['username'] = username
	record['days'] = days

	if username in uname_map and 'name' in uname_map[username]:
		record['name'] = uname_map[username]['name']

	output.append(record)

print(json.dumps({'ranking':output}))
