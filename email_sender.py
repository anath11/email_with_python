import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Python Email'
email['to'] = 'nathashok87@gmail.com'
email['subject'] = 'You won a million dollar from a broke ass lottery ticket'

email.set_content(
    'I am Python devloper. \nLearning to script from this language')

with smtplib.SMTP(host='smtp.yahoo.com', port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('emailpython@yahoo.com', 'Send@message1')
    smtp.send_message(email)
    print('all good boss email sent!')

# Send@message1
