#!/usr/bin/python
from twilio.rest import TwilioRestClient
import cgi

inputs = cgi.FieldStorage()

if 'sid' in inputs and 'token' in inputs and 'str_list' in inputs and 'from_num' in inputs and 'to_num' in inputs:
	account_sid = inputs['sid'].value
	auth_token = inputs['token'].value
	body_list = inputs.getlist('str_list')
	to_num = '+'+inputs['to_num'].value
	if len(to_num) != 12:
		# assume 1 dropped
		to_num = '+1' + to_num[1:]
	from_num = '+'+inputs['from_num'].value

	body = ''
	for s in body_list:
		body += s + '\n'

	client = TwilioRestClient(account_sid, auth_token)

	message = client.sms.messages.create(body=body,
			to=to_num,
			from_=from_num)
	print 'Success!'

