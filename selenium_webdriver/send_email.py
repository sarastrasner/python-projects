import smtplib
import os

EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

def send_email(list):
    print('after line 6')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # Connects with GMAIL
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL, PASSWORD)

        subject = 'Found a dill!'  # Subject and body defined in code = works
        body = f'Found some adjustable dumbbells on sale for: {list}'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL, "girliesara22@yahoo.com", msg)
