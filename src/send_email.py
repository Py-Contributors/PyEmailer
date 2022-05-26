import smtplib
import email.message

import re

server = smtplib.SMTP('smtp.gmail.com:587')
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def checkEmail(email):
    if(re.search(regex, email)):
        return True
    else:
        return False

# https://myaccount.google.com/security to get app_password

def sendEmail(your_email_id: str, your_app_password: str, 
              email_subject: str, email_content: str, listOfEmail: list):
    
    """ Send email to list of email id
    
    Args:
        your_email_id: Email id of sender
        your_app_password: App password of sender
        email_subject: Subject of email
        email_content: Content of email
        listOfEmail: List of email id to send email
     """
    msg = email.message.Message()
    msg['Subject'] = email_subject
    msg['From'] = your_email_id
    password = your_app_password

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
            print("sending to {}".format(destinationEmail))
        else:
            print("[INFO]: {} is not a valid email.".format(destinationEmail))
    
    