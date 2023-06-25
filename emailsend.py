import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = "20102106.namratanarkhede@gmail.com"
password = "20102106NN"

message = """

        <html>
                	<head>
                		<meta charset="utf-8" />
                		<title></title>
                	</head>
                	<body>
                		<h1>helloooo</h1>
                	</body>
                </html>

            """
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    msg = MIMEMultipart("alternative")
    msg.attach(MIMEText(message, 'html'))
    msg['Subject'] = 'you did it '
    msg['From'] = my_email
    msg['To'] = "namratanarkhede10@gmail.com"
    smtp.starttls()
    smtp.login(user=my_email, password=password)
    smtp.sendmail(
        from_addr=my_email,
        to_addrs="namratanarkhede10@gmail.com",
        msg=msg.as_string()
    )
