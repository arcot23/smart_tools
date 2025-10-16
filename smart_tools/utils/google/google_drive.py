from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path

def upload_file(file, folder_id):
    # Scopes for full Drive access
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    TOKEN_PATH = 'token.json'  # This must contain a valid refresh token

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': Path(file).stem,
    'parents': [folder_id]
}
    media = MediaFileUpload(file, mimetype='text/csv')

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"Uploaded file ID: {file.get('id')}")


def main():
    upload_file(rf"C:\temp\events-Events in NJ.csv", "1DinA0h8EOBCUstV1-cQKHMO3mji-OdCS")


if __name__ == "__main__":
    main()