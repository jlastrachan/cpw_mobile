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

def search_table_day_time(cnx, day, time):
	cursor = cnx.cursor()
	query = ("SELECT id FROM events "
		"WHERE day = %s AND startTime <= %s AND endTime >= %s")
	cursor.execute(query, (day, time, time))
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
	if event_type == 'false':
		print toAngelXML(search_table_day_time(cnx, day, time))
	else:
		print toAngelXML(sesarch_table_type(cnx, event_type))
else:
	day = "Thursday"
	time = "12:00:00"
	print toAngelXML(search_table_day_time(cnx, day, time))
	
close_table(cnx)
