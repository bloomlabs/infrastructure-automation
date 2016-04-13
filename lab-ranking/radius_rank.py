# Parses freeradius authentication logs to generate stats about presence in lab
# Configure in crontab to write to http://<website>/ranking.json to be read by bubble-rank.html
# Using Python 3.3+
import gzip, glob, datetime, re, itertools, json
import pymysql.cursors
from auth_secret import * # Import RADIUS_USER and RADIUS_PASS

CUR_DIR = "/var/log/freeradius/"
logex = re.compile("^(.*?) : Auth: Login OK: \[(.*?)\] .*?$")

cnx = pymysql.connect(user=RADIUS_USER, password=RADIUS_PASS,
                              host='127.0.0.1',
                              database='radiusdb')
uname_map = {}
with cnx.cursor() as cursor:
	cursor = cnx.cursor()
	cursor.execute("SELECT username, firstname, lastname FROM userinfo")
	for username, firstname, lastname in cursor.fetchall():
		username = username.lower()

		if firstname or lastname:
			if firstname and lastname:
				uname_map[username] = firstname + " " + lastname
			elif firstname:
				uname_map[username] = firstname
			elif lastname:
				uname_map[username] = lastname

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

	if username in uname_map:
		record['name'] = uname_map[username]

	output.append(record)

print(json.dumps({'ranking':output}))