# Generated by Django 4.2.6 on 2024-05-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_tempverifycode_user_try_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempResetCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_code', models.CharField(help_text='Code used in the URL to change the password.', max_length=32)),
                ('user_id', models.IntegerField(help_text='User Id - used to identify the user')),
            ],
        ),
    ]
