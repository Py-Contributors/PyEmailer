"""
# Usages
# python commandLineEmailScript.py destination@email.com 
"""
import smtplib
import email.message
import fire
server = smtplib.SMTP('smtp.gmail.com:587')

from JuneContent import content

def sendEmail(destinationEmail):
    email_content = content

    msg = email.message.Message()
    msg['Subject'] = 'your_subject_here'  #write the subject of your mail here
    msg['From'] = 'youEmail@gmail.com'    #write your email address here
    password = "your gmail app password"   # create app password in accounts/security and paste here
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

     
    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    #sending email one by one to each email ID in the list

    s.sendmail(msg['From'], destinationEmail, msg.as_string())
    print(f"sending to {destinationEmail}")


fire.Fire(sendEmail)
print("Email/s successfully sent. Please check your sentbox for confirmation.")

