import os
from email.message import EmailMessage
import smtplib
import datetime as dt
import time

def send_email():
    email_user = 'amittyardeni@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'AMITyardeni')

    #EMAIL
    message = 'Good Morning'
    email = EmailMessage()
    email['From'] = email_user
    email['To'] = '*****@gmail.com'
    email['Subject'] = 'Very Important Message'
    email.set_content(message)
    server.send_message(email)
    server.quit()


send_email()



