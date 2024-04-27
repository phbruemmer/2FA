from django.db import models


class User(models.Model):
    username = models.CharField(
        max_length=20,
        help_text='Defines Username')
    user_email = models.EmailField(
        help_text='Defines Email')
    user_password = models.CharField(
        max_length=60,
        help_text='Defines User Password - Encrypted and verified')

    def str(self):
        return self.username

