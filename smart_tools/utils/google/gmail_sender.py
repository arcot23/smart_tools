from __future__ import print_function
import os.path
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def send_email(sender='sender@gmail.com',
               to='receiver@gmail.com',
               subject='Hello from Gmail API',
               message_text='This email was sent using OAuth tokens without any prompts!',
               email_type="plain"):
    # Load saved OAuth credentials
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    TOKEN_PATH = 'token.json'  # This must contain a valid refresh token

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Build Gmail API client
    service = build('gmail', 'v1', credentials=creds)

    # Create email message
    def create_message(sender, to, subject, message_text, email_type="plain"):
        message = MIMEText(message_text, email_type)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    # Send email
    message = create_message(
        sender,
        to,
        subject,
        message_text,
        email_type
    )

    sent = service.users().messages().send(userId='me', body=message).execute()
    print(f"Email sent! Message ID: {sent['id']}")

def main():
    send_email()

if __name__ == "__main__":
    main()