![header](https://capsule-render.vercel.app/api?type=wave&color=gradient&height=300&section=header&text=PyEmailer&fontSize=50)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
![issues](https://img.shields.io/github/issues/codePerfectPlus/PyEmailer?style=plastic)
![forks](https://img.shields.io/github/forks/codePerfectPlus/PyEmailer)
![stars](https://img.shields.io/github/stars/codePerfectPlus/PyEmailer)
![License](https://img.shields.io/github/license/codePerfectPlus/PyEmailer)

![Visitor Count](https://profile-counter.glitch.me/PyEmailer/count.svg)

**Blog On Python, Machine Learning and Data Science Visit [CodePerfectPLus](http://codeperfectplus.herokuapp.com/)**

## Create App Password in gmail.

- GO to Account [setting/Security](https://myaccount.google.com/security)
- click app password
- Select APP -> others, Select Device -> Others
- Copy paste the code in script.py `password` variable


## Usage

```bash
git clone https://github.com/codePerfectPlus/PyEmailer
cd PyEmailer
```

```python
from src.send_email import PyEmailer

your_email_id = "your_email_id"
your_app_password = "your_app_password"
email_subject = "email_subject_here"
email_content = "<h1> Email Content can be html too</h1>"
listOfEmail = ["destination1@gmail.com", "destination2@gmail.com"]

pyemail = PyEmailer(your_email_id, your_app_password)

if __name__ == "__main__":
    pyemail.sendEmail(email_subject, email_content, listOfEmail)
```

## Upcoming features

- file attachment in email
- ~~RegEx to verify the Emails~~

### Project

- Project: PyEmailer
- Author: CodePerfectPlus
- Language: Python
- Github: https://github.com/codePerfectPlus
- Website: http://codeperfectplus.herokuapp.com/
