import dotenv
import os

from sys import stdout
from datetime import datetime
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

dotenv.load_dotenv()


class Envs:
    EMAIL_HOST_USERNAME = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_FROM = os.getenv('EMAIL_FROM')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
    EMAIL_SERVER = os.getenv('EMAIL_SERVER')


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.EMAIL_HOST_USERNAME,
    MAIL_PASSWORD=Envs.EMAIL_HOST_PASSWORD,
    MAIL_FROM=Envs.EMAIL_FROM,
    MAIL_PORT=Envs.EMAIL_PORT,
    MAIL_SERVER=Envs.EMAIL_SERVER,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True
)


async def send_email_async(subject: str, body: str, receiver: str):
    stdout.write(f'{datetime.now()}: creating message instance...\n')
    message = MessageSchema(
        subject=subject,
        recipients=[receiver],
        body=body,
        subtype=MessageType.plain
    )
    stdout.write(f'{datetime.now()}: created.\n')
    stdout.write(f'{datetime.now()}: connecting to smtp.gmail.com...\n')
    fm = FastMail(conf)
    stdout.write(f'{datetime.now()}: sending message...\n')
    await fm.send_message(message)
    stdout.write(f'{datetime.now()}: successfully sent message...\n')
