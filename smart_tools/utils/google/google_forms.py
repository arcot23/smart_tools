from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def get_form(form_id='1VOTlDvzIiOFHCwnPI6FSVBBMwgA22E54t_rg0cDheog'):
    SCOPES = ['https://www.googleapis.com/auth/forms.body.readonly']
    TOKEN_PATH = 'token.json'  # This must contain a valid refresh token

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Build Forms API client
    service = build('forms', 'v1', credentials=creds)

    # Make the API call to get the form
    form = service.forms().get(formId=form_id).execute()

    print(rf"formId: {form['formId']}")
    print(rf"info: {form['info']}")


    for item in form['items']:
        # print([key for key in iter(item.keys)])
        if 'title' in item:
            print(f"Title: {item['title']}")
        # if 'questionItem' in item:
        #     question = item['questionItem']['question']
        #     print(f"Question ID: {question['questionId']}, Text: {question['textQuestion']}")

def get_form_respondents_emails(form_id='1VOTlDvzIiOFHCwnPI6FSVBBMwgA22E54t_rg0cDheog'):
    SCOPES = ['https://www.googleapis.com/auth/forms.responses.readonly']
    TOKEN_PATH = 'token.json'  # This must contain a valid refresh token

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Build Forms API client
    service = build('forms', 'v1', credentials=creds)

    # Make the API call to get the form
    result = service.forms().responses().list(formId=form_id).execute()

    email_addresses = []
    if "responses" in result:
        email_addresses = [response['respondentEmail'] for response in result["responses"]]

    return "; ".join(email_addresses)


def get_form_responses(form_id='1VOTlDvzIiOFHCwnPI6FSVBBMwgA22E54t_rg0cDheog'):
    SCOPES = ['https://www.googleapis.com/auth/forms.responses.readonly']
    TOKEN_PATH = 'token.json'  # This must contain a valid refresh token

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Build Forms API client
    service = build('forms', 'v1', credentials=creds)

    # Make the API call to get the form
    result = service.forms().responses().list(formId=form_id).execute()
    if "responses" in result:
        print(rf"Responses: {len(result['responses'])}")
        for response in result["responses"]:
            print(f"Response ID: {response['responseId']}")
            print(f"RespondentEmail: {response['respondentEmail']}")
            # Process individual answers within the response
            for item_response in response.get('answers', {}).values():
                question_id = item_response['questionId']
                # Assuming text answers for simplicity
                text_answers = item_response['textAnswers']['answers'][0]['value']
                print(f"  Question ID: {question_id}, Answer: {text_answers}")
    else:
        print(rf"Responses: 0")


def main():
    get_form()


if __name__ == "__main__":
    main()
