# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC18450101a083b59de2e8597a6ba81ae5"
auth_token = "3729f944ff2eb413323457ffc70af767"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+919840115377",
    from_="+919176199192",
    body="Hello Ji!")