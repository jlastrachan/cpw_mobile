#!/usr/bin/python
import mysql.connector
import cgi
import datetime
from datetime import time
print 'Content-Type: text/html'
print

def open_table():
	config = {
		'user': 'jennya',
		'password': 'ruy11xir',
		'host': 'sql.mit.edu',
		'database': 'jennya+cpw_mobile',
		'raise_on_warnings': True,
	}
	cnx = mysql.connector.connect(**config)
	return cnx

def search_table(cnx, day, time, type):
	cursor = cnx.cursor()
	sets = []
	if day == 'false' and time == 'false' and type == 'false':
		query = 'SELECT id FROM events;'
		cursor.execute(query)
		result = [id for (id,) in cursor]
		return result
	if day != 'false':
		query = 'SELECT id FROM events WHERE day="%s";' % day
		cursor.execute(query)
		result = set([id for (id,) in cursor])
		if time != 'false':
			query = 'SELECT id FROM events WHERE endTime>="%s";' % time
			cursor.execute(query)
			time_result = set([id for (id,) in cursor])
			result = result.intersection(time_result)
			if int(time[:time.index(':')]) >= 19:
				query = 'SELECT id FROM events WHERE startTime >="3:00:00" AND endTime<="3:00:00" AND day="%s";' % day
				cursor.execute(query)
				new_day_result = [id for (id,) in cursor]
				result = result.union(set(new_day_result))
		sets.append(result)
	if type != 'false':
		query = 'SELECT id FROM events WHERE %s="True";' % type
		cursor.execute(query)
		result = [id for (id,) in cursor]
		sets.append(set(result))
	if len(sets) == 0:
		return sets
	result = sets[0]
	for s in sets:
		result = result.intersection(s)
	cursor.close()
	return sorted(list(result))

def close_table(cnx):
	cnx.close()

def toAngelXML(id_list):
	xmlstring = """<ANGELXML><MESSAGE><PLAY>"""
	xmlstring += '<PROMPT type=\"text\">.</PROMPT>' + """</PLAY>\n"""
	xmlstring += '<GOTO destination="/20" />'
	xmlstring += """</MESSAGE><VARIABLES><VAR name="idList" value=""" + '"'
	for i in range(len(id_list)):
		xmlstring += str(id_list[i])
		if i < len(id_list) - 1:
			xmlstring += ', '
	xmlstring += '" type="list" separator=","/>\n' + """</VARIABLES></ANGELXML>"""
	return xmlstring

inputs = cgi.FieldStorage()
cnx = open_table()

days = ['Thursday', 'Friday', 'Saturday', 'Sunday']
event_types = ['featured', 'food', 'party', 'academic', 'class', 'tour', 'dorm', 'livinggroup', 'studentorg', 'parents', 'religious', 'minority', 'arts', 'athletic']

if 'day' in inputs and 'time' in inputs and 'type' in inputs:
	day = inputs['day'].value
	time = inputs['time'].value
	if day.find('/') != -1:
		m, d, y = (int(x) for x in day[:day.index(' ')].split('/'))    
		ans=datetime.date(y,m,d)
		day_index = ans.weekday()
		day = 'Thursday'
		if day_index >= 3:
			day = days[day_index-3]

		time = time[time.index(' ') + 1:]
	if 'pm' in time or 'am' in time:
		if 'pm' in time:
			hour = time[:time.index(':')]
			if int(hour) != 12:
				hour = int(hour)  + 12
			time = str(hour)+time[time.index(':'):]
		if 'am' in time:
			hour = time[:time.index(':')]
			if int(hour) == 12:
				time = time = '00' + time[time.index(':'):]
		time = time[:time.index(' ')]
		time += ':00'
	event_type = inputs['type'].value
	if event_type == 'all' or event_type not in event_types:
		event_type = 'false'
	print toAngelXML(search_table(cnx, day, time, event_type))
else:
	day = "Friday"
	time = "16:00:00"
	if day.find('/') != -1:
		m, d, y = (int(x) for x in day[:day.index(' ')].split('/'))    
		ans=datetime.date(y,m,d)
		day_index = ans.weekday()
		day = 'Thursday'
		if day_index >= 3:
			day = days[day_index-3]

		time = time[time.index(' ') + 1:]

	type = 'food'
	print toAngelXML(search_table(cnx, day, time, type))
	
close_table(cnx)
