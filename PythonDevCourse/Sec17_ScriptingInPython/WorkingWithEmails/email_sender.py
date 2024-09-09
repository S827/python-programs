import smtplib  # smtp : simple mail transfer protocol
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Eto Svn'
email['to'] = 'shaktiv827@gmail.com'
email['subject'] = 'Test Subject'

email.set_content('This is test content')
email1 = EmailMessage()
email1['from'] = 'Eto Svn'
email1['to'] = 'dskumar827@gmail.com'
email1['subject'] = 'You have won 1000000$'
email1.set_content('Enjoy your money. hahahahahahha!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    print('hello')
    smtp.ehlo()
    smtp.starttls()  # tls: encryption mechanism
    smtp.login('nametest230@gmail.com', 'lvdc abhp hnny lxyo')
    smtp.send_message(email)
    smtp.send_message(email1)
    print('Done')
