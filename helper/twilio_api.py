import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID_PROD')
auth_token = os.getenv('TWILIO_AUTH_TOKEN_PROD')

if not account_sid or not auth_token:
    raise ValueError("Twilio credentials not found in environment variables.")
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )

