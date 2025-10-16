#  python -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/forms.body.readonly',
          'https://www.googleapis.com/auth/forms.responses.readonly', 'https://www.googleapis.com/auth/drive.file']

flow = InstalledAppFlow.from_client_secrets_file('../../../credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
with open('../../../token.json', 'w') as token:
    token.write(creds.to_json())
