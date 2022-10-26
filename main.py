from src.send_email import PyEmailer

your_email_id = "your_email_id"
your_app_password = "your_app_password"
email_subject = "email_subject_here"
email_content = "<h1> Email Content can be html too</h1>"
listOfEmail = ["destination1@gmail.com", "destination2@gmail.com"]

pyemailer = PyEmailer(your_email_id, your_app_password)

if __name__ == "__main__":
    pyemailer.sendEmail(email_subject, email_content, listOfEmail)
