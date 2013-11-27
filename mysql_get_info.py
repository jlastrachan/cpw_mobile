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

def search_table_id(cnx, id):
	cursor = cnx.cursor()
	query = ("SELECT name, startTime, endTime, location, description, day FROM events "
		"WHERE id=%s")
	cursor.execute(query, (id,))
	result = None
	for (name, start, end, location, desc, day) in cursor:
		# IDs are unique, so return first one.
		result = {'name': name, 'startTime': start, 'endTime': end, 'location': location, 'description': desc, 'day': day}
	cursor.close()
	return result
	
def close_table(cnx):
	cnx.close()

def toAngelXML(info, page):
	demo = '<PROMPT type=\"text\">.</PROMPT>'
	xmlstring = """<ANGELXML><MESSAGE><PLAY>"""
	xmlstring += demo + """</PLAY>\n"""
	xmlstring += '<GOTO destination="/' + str(page)+'" />'
	xmlstring += """</MESSAGE><VARIABLES><VAR name=\"curr_name\" value="""
	xmlstring += '"' + info['name'] + '"' + """/> 
	    <VAR name="curr_day" value=""" + '"'
	xmlstring += info['day'] + '"' + """/>
	    <VAR name="curr_startTime" value="""
	xmlstring += '"' + info['startTime'] + '"' + """/>
	    <VAR name="curr_endTime" value="""
	xmlstring += '"' + info['endTime'] + '"' + """/>
	    <VAR name="curr_location" value="""
	xmlstring += '"' + str(info['location']) + '"' + """/>
	    <VAR name="curr_description" value="""
	xmlstring += '"' + str(info['description']) + '"' + """/>\n"""
	xmlstring += """</VARIABLES></ANGELXML>"""
	return xmlstring

inputs = cgi.FieldStorage()
cnx = open_table()

if 'id' in inputs and 'page' in inputs:
	id = inputs['id'].value
	page = inputs['page'].value
	print toAngelXML(search_table_id(cnx, id), page)
else:
	id = "1"
	page = "15"
	print toAngelXML(search_table_id(cnx, id), page)
	
close_table(cnx)
