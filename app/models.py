from django.db import models
from django.utils import timezone


class TempUser(models.Model):
    username = models.CharField(
        max_length=20,
        help_text='Defines Username')
    user_email = models.EmailField(
        help_text='Defines Email')
    user_password = models.CharField(
        max_length=60,
        help_text='Defines User Password - Encrypted and verified')


class RegisteredUser(models.Model):
    username = models.CharField(
        max_length=20,
        help_text='Defines Username')
    user_email = models.EmailField(
        help_text='Defines Email')
    user_password = models.CharField(
        max_length=60,
        help_text='Defines User Password - Encrypted and verified')
    registration_date = models.DateTimeField(default=timezone.now, help_text='Registration Date')


class TempURL(models.Model):
    verification_code = models.CharField(max_length=32,
                                         help_text='Verification Code to verify the user')
    username = models.CharField(max_length=20)




