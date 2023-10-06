from fastapi import FastAPI, Response
from send_mail import send_email_async
from validators import SendEmail
from sys import stdout
from datetime import datetime

app = FastAPI()


@app.post("/send_email")
async def send_email(body: SendEmail):
    stdout.write(f'{datetime.now()}: received send_email request, processing...\n')
    await send_email_async(body.subject, body.message, body.to)
    stdout.write(f'{datetime.now()}: successfully processed request.\n')
    return Response(status_code=200)


