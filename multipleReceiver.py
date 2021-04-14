import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')

listofemail =  ["destination1@gmail.com", "destination2@gmail.com"] # List of Email id for sending emails

email_content = "<h1> Email Content can be html too</h1>"

# get email_app_password from account/security 
# https://myaccount.google.com/security
def sendEmail():
    msg = email.message.Message()
    msg['Subject'] = 'email_subject_here'  # write the subject of your mail here
    msg['From'] = 'youEmail@gmail.com'    # write your email address here
    password = "your gmail app password"   # create app password in accounts/security and paste here
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

     
    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    #sending email one by one to each email ID in the list
    for dest in listofemail:
        s.sendmail(msg['From'], dest, msg.as_string())
        print(f"sending to {dest}")

if __name__ == '__main__':
    sendEmail()
    print("Email/s successfully sent. Please check your sentbox for confirmation.")
