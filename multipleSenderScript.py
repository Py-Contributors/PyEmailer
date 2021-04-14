import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')

from checkemail import checkEmail

email_content = "<h1>Hi This content can be in the Html format.</h1>"
destinationEmail = "destination@live.com"

senderEmails = {"sender1@gmail.com": "app_password", "sender2@gmail.com": "app_password"}

print(f"[INFO]: Sending to {destinationEmail}")

# https://myaccount.google.com/security to get app_password
def sendEmail():
    for key, value in senderEmails.items():
        msg = email.message.Message()
        msg['Subject'] = 'msg_subject_here'
        msg['From'] = key
        password = value
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        # Login Credentials for sending the mail
        s.login(msg['From'], password)

        if checkEmail(destinationEmail):
            s.sendmail(msg['From'], destinationEmail, msg.as_string())
            print(f"[INFO]: Sending msg from {key}")
        else:
            print(f"[INFO]: {destinationEmail} is not a valid email")

if __name__ == '__main__':
    sendEmail()