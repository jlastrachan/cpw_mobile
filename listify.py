#!/usr/bin/python

import cgi

# Start by getting variables:
inputs = cgi.FieldStorage()
if 'myarray' in inputs:
	myarray = inputs['myarray'].value
else:
	myarray = 'test1,test2'

# Make page for Angel. 
print 'Content-Type: text/html'
print 
print '<ANGELXML>' 
print '<MESSAGE>' 
print '<PLAY>' 
print '<PROMPT type="text">.' # no prompt 
print '</PROMPT>' 
print '</PLAY>' 
print '<GOTO destination="/1" />' # have to say the page number!!! 
print '</MESSAGE>' 
print '<VARIABLES>' 
print '<VAR name="myarrayasastring" value="' + myarray + '" type="list" separator="," />' 
print '</VARIABLES>' 
print '</ANGELXML>' 

