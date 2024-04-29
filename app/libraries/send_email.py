from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'phbruemmer0@gmail.com'
email_password = 'sddm dpff fgyi kpai'
email_receiver = 'phbruemmer@gmail.com'


def send(subject, body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def send_verification(username, custom_str):
    subject = 'Verify your Account'
    body = f"""
    This is an automated email.
    Please verify your account by clicking on this link:
    http://192.168.115.52:8000/verify/{username}/{custom_str}/
    """
    send(subject, body)


def send_2FA_code(code):
    subject = 'Login Code for verification'
    body = f"""
    This is an automated email.
    Enter the following code to verify your login attempt:
    {code}"""
    send(subject, body)
