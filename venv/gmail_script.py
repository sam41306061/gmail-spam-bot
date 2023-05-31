from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow



SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
creds = None

def auth():
    global creds
    flow = InstalledAppFlow.from_client_secrets_file(
        ', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds
