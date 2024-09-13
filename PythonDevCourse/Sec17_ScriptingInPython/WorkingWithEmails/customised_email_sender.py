import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, TO_EMAIL, TO_EMAIL1  # type: ignore

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Eto Svn'
email['to'] = TO_EMAIL
email['subject'] = 'Yo! You have won 1000000$'
email.set_content(html.substitute({'name': 'Divya'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.send_message(email)
    print('Email Sent')
