import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow # local launch of api 
from googleapiclient.discovery import build
# optional
import googleapiclient.errors
# import HttpError


CLIENT_FILE = 'gmail-bot-yosemite.json'
SCOPES = ['https://mail.google.com/']

creds = None # access token

if os.path.exists('token.json'):
    credit = Credentials.from_authorized_user_file('gmail-bot-yosemite.json', SCOPES)

if not creds or not creds.vali:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())