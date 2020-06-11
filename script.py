import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')

from JuneContent import content
from emaillist import emails

email_content = content
listofemail =  emails # List of Email id for sending emails

msg = email.message.Message()
msg['Subject'] = 'Codeperfectplus DataScience Newsletter'
msg['From'] = 'youEmail@gmail.com'
password = "your gmail app password"   # create app password in accounts/security
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

 
# Login Credentials for sending the mail
s.login(msg['From'], password)

for dest in listofemail:
    s.sendmail(msg['From'], dest, msg.as_string())
    print(f"sending to {dest}")
