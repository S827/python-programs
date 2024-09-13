import smtplib  # smtp : simple mail transfer protocol
from email.message import EmailMessage
from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, TO_EMAIL, TO_EMAIL1  # type: ignore

email = EmailMessage()
email['from'] = 'Eto Svn'
email['to'] = TO_EMAIL
email['subject'] = 'Test Subject'

email.set_content('This is test content')
email1 = EmailMessage()
email1['from'] = 'Eto Svn'
email1['to'] = TO_EMAIL1
email1['subject'] = 'You have won 1000000$'
email1.set_content('Enjoy your money. hahahahahahha!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    print('hello')
    smtp.ehlo()
    smtp.starttls()  # tls: encryption mechanism
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.send_message(email)
    smtp.send_message(email1)
    print('Done')
