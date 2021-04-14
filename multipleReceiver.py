import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')

from checkemail import checkEmail

# List of Email id for sending emails
listOfEmail =  ["destination1@gmail.com", "destination2@gmail.com"]

email_content = "<h1> Email Content can be html too</h1>"

# https://myaccount.google.com/security to get app_password
def sendEmail():
    msg = email.message.Message()
    msg['Subject'] = 'email_subject_here'
    msg['From'] = 'youEmail@gmail.com'
    password = "your gmail app password"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    # sending email one by one to each email ID in the list
    for destinationEmail in listOfEmail:
        if checkEmail(destinationEmail):
            s.sendmail(msg['From'], destinationEmail, msg.as_string())
            print(f"sending to {destinationEmail}")
        else:
            print(f"[INFO]: {destinationEmail} is not a valid email.")

if __name__ == '__main__':
    sendEmail()
    print("Email/s successfully sent. Please check your sentbox for confirmation.")
