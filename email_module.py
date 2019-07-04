import os
import smtplib
import credentials as cd
from email.message import EmailMessage

def emailFunc(From, To, subject, body):

    EMAIL_ID = From
    EMAIL_PASS = cd.cred

    msg = EmailMessage()
    msg['From'] = EMAIL_ID
    msg['To'] = To
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ID,EMAIL_PASS)
        smtp.send_message(msg)