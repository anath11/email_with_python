import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Oryx Ratana'
email['to'] = 'nathashok87@gmail.com'
email['subject'] = 'You won a million dollar from a broke ass lottery ticket'

email.set_content(
    'I am Python devloper. \nLearning to script from this language')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ratana.oryx@gmail.com', 'Alpha123A!')
    smtp.send_message(email)
    print('all good boss email sent!')
