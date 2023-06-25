import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Namrata Narkhede'
email['to'] = 'namratanarkhede10@gmail.com'
email['subject'] = 'Congratulation!!'

email.set_content(html.substitute(name = 'namrata'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('20102106.namratanarkhede@gmail.com', '20102106NN')
    smtp.send_message(email)
    print('done done done')
