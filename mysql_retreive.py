#!/usr/bin/python
import mysql.connector
import cgi
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
	query_str = ''
	if day is not 'no':
		query_str += 'day = %s' % day
	if time is not 'no':
		if query_str is not '':
			query_str += ' AND '
		query_str += 'endTime >= %s' % time
	if type is not 'no':
		if query_str is not '':
			query_str += ' AND '
		query_str += '%s=True' %s type

	query = ("SELECT id FROM events WHERE " + query_str)
	cursor.execute(query)
	result = [id for (id,) in cursor]
	cursor.close()
	return result
	
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
if 'day' in inputs and 'time' in inputs and 'type' in inputs:
	day = inputs['day'].value
	time = inputs['time'].value
	if 'pm' in time or 'am' in time:
		if 'pm' in time:
			hour = time[:time.index(':')]
			hour = int(hour)  + 12
			time = str(hour)+time[time.index(':'):]
		time = time[:time.index(' ')]
		time += ':00'
	event_type = inputs['type'].value
	print toAngelXML(sesarch_table(cnx, day, time, event_type))
else:
	day = "Thursday"
	time = "12:00:00"
	type = 'no'
	print toAngelXML(search_table(cnx, day, time, type))
	
close_table(cnx)
