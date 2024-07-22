import smtplib, ssl
import os


PASSWORD = os.getenv("GOOGLEPASSWORD")  # need to first input environmental variable in os
USERNAME = "ryankaufman79@gmail.com"
RECEIVER = "ryankaufman79@gmail.com"


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, RECEIVER, message)
