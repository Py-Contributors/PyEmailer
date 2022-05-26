from src.send_email import sendEmail

your_email_id = "your_email_id"
your_app_password = "your_app_password"
email_subject = "email_subject_here"
email_content = "<h1> Email Content can be html too</h1>"
listOfEmail =  ["destination1@gmail.com", "destination2@gmail.com"]

if __name__ == "__main__":
    sendEmail(your_email_id, your_app_password, 
              email_subject, email_content, listOfEmail)
