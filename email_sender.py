import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Python Email'
email['to'] = 'nathashok87@gmail.com'
email['subject'] = 'You won a million dollar from a broke ass lottery ticket'

email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('emailpython39@gmail.com', 'SendEmail1')
    smtp.send_message(email)
    print('all good boss email sent!')


# Send@message1
