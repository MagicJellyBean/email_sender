from smtplib import SMTP
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Karol'
email['to'] = 'someones@email.com'
email['subject'] = 'Email sender'

email.set_content(html.substitute({'name': 'Someone'}), 'html')

with SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Using gmail you have to find option 'passwords for applications'
    # And using that unique password login to gmail:
    smtp.login('email@gmail.com', 'password')
    smtp.send_message(email)
