import smtplib
import email.message

import re

server = smtplib.SMTP('smtp.gmail.com:587')
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def checkEmail(email):
    if re.search(regex, email):
        return True
    else:
        return False


class PyEmailer(object):
    """
    Class to send email using python

    methods:
        sendEmail: Send email to list of email id

    """
    def __init__(self, your_email_id, your_app_password):
        self.your_email_id = your_email_id
        self.your_app_password = your_app_password

    def sendEmail(self, email_subject: str,
                  email_content: str, listOfEmail: list) -> dict:

        """ Send email to list of email id

        Args:
            email_subject: Subject of email
            email_content: Content of email
            listOfEmail: List of email id to send email
        """
        output = {'success': 0, 'failed': 0, 'invalid': 0}

        msg = email.message.Message()
        msg['Subject'] = email_subject
        msg['From'] = self.your_email_id
        password = self.your_app_password

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        server.login(msg['From'], password)

        # sending email one by one to each email ID in the list
        for destinationEmail in listOfEmail:
            if checkEmail(destinationEmail):
                try:
                    server.sendmail(msg['From'], destinationEmail, msg.as_string())
                    print("sending to {}".format(destinationEmail))
                    output['success'] += 1
                except Exception as e:
                    print("Error: {}".format(e))
                    output['failed'] += 1
            else:
                print("[INFO]: {} is not a valid email.".format(destinationEmail))
                output['invalid'] += 1

        return output
