from twilio.rest import TwilioRestClient
import cgi

inputs = cgi.FieldStorage()

if 'sid' in inputs and 'token' in inputs and 'message' in inputs and 'from_num' in inputs and 'to_num' in inputs:
	account_sid = inputs['sid'].value
	auth_token = inputs['location'].value
	body = inputs['message'].value
	to_num = '+'+inputs['to_num'].value
	from_num = '+'+inputs['from_num'].value

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body=body,
			to=to_num,
			from_=from_num)
