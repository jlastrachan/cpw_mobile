#!/usr/bin/python
import mysql.connector
import os

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

def make_insert_string(name, start_time, day, end_time, location, description, type_dict):
	result = "INSERT INTO events (name, startTime, endTime, day, location, description, "
	for type in type_dict:
		result += type + ', '
	result = result[:-2] + ') VALUES ('
	result += '"' + name + '",'
	result += '"' + start_time + '",'
	result += '"' + end_time + '",'
	result += '"' + day + '",'
	result += '"' + location + '",'
	result += '"' + description + '",'
	for (type, val) in type_dict.items():
		result += '"' + str(val) + '",'
	result = result[:-1] + ');'
	print result
	return result
	
def close_table(cnx):
	cnx.close()

cnx = open_table()
f = open('cpw_events.csv')
file = f.readline()
for line in file.split('%%'):
	items = line.split('|')
	day = items[0].strip()
	start_time = items[1].strip()
	end_time = items[2].strip()
	name = items[3].strip()
	location = items[4].strip()
	description = items[5].strip()
	types = items[6:]
	for i in range(len(types)):
		types[i] = types[i].strip()
	type_dict = {}
	type_list = ['food', 'party', 'featured', 'minority', 'studentorg', 'dorm', 'livinggroup', 'academic', 'athletic', 'class', 'arts', 'parents', 'tour', 'religious']
	for type in type_list:
		type_dict[type] = (type in types)	
	cursor = cnx.cursor()
	query = (make_insert_string(name, start_time, day, end_time, location, description, type_dict))
	cursor.execute(query)
	cursor.close()
'''
day = 'Thursday'
start_time = '12:00:00'
end_time = '13:00:00'
name = 'event'
location = 'place'
description = 'event description'
types = ['featured', 'academic', 'parents']
type_dict = {}
type_list = ['featured', 'minority', 'studentorg', 'dorm', 'livinggroup', 'academic', 'athletic', 'class', 'arts', 'parents', 'tour', 'religious']
for type in type_list:
	type_dict[type] = (type in types)	
print make_insert_string(name, start_time, day, end_time, location, description, type_dict)
'''
close_table(cnx)
