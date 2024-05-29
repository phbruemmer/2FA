from .send_email import send


def send_verification(username, custom_str):
    subject = 'Verify your Account'
    body = f"""
    This is an automated email.
    Please verify your account by clicking on this link:
    http://127.0.0.1:8000/accounts/verify/{username}/{custom_str}/"""
    send(subject, body)


def send_2FA_code(code):
    subject = 'Login Code for verification'
    body = f"""
    This is an automated email.
    Enter the following code to verify your login attempt:
    {code}"""
    send(subject, body)


def send_reset_request(user_id, code):
    subject = 'password reset request'
    body = f"""
    This is an automated email.
    You can change your password after clicking on this link:
    http://127.0.0.1:8000/accounts/recover/{user_id}/{code}/
    """
    send(subject, body)
