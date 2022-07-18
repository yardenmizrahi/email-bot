import os
import random
from email.message import EmailMessage
import smtplib
import datetime as dt
import time
from quote import quote


def send_email():
    email_user = 'amittyardeni@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'AMITyardeni')

    #EMAIL
    quotes = quote("William Shakespeare", limit=50)
    body = random.sample(quotes, k=1)[0]['quote']
    email = EmailMessage()
    email['From'] = email_user
    email['To'] = "*****@gmail.com"
    email['Subject'] = "Quote of the Day"
    email.set_content(body)
    server.send_message(email)
    server.quit()


send_email()

