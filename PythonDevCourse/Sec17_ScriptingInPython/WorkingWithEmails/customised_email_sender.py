import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Eto Svn'
email['to'] = 'shaktiv827@gmail.com'
email['subject'] = 'Yo! You have won 1000000$'
email.set_content(html.substitute({'name': 'Divya'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nametest230@gmail.com', 'lvdc abhp hnny lxyo')
    smtp.send_message(email)
    print('Email Sent')
