#!/usr/bin/python

import cgi

# Start by getting variables:
inputs = cgi.FieldStorage()
if 'myarray' in inputs:
	myarray = inputs.getlist('myarray')
else:
	myarray = []
mystring = ''
for elt in myarray:
	mystring += elt + ','
mystring = mystring[:-1]

# Make page for Angel. 
print 'Content-Type: text/html'
print 
print '<ANGELXML>' 
print '<MESSAGE>' 
print '<PLAY>' 
print '<PROMPT type="text">.' # no prompt 
print '</PROMPT>' 
print '</PLAY>' 
print '<GOTO destination="/42" />' # have to say the page number!!! 
print '</MESSAGE>' 
print '<VARIABLES>' 
print '<VAR name="myarrayasastring" value="' + mystring + '"/>' 
print '</VARIABLES>' 
print '</ANGELXML>' 

