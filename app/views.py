from django.http import HttpResponse
from django.shortcuts import render

from .libraries import register_user_verification
from .models import *


def main(request):
    return HttpResponse('<center><h1>404</h1><br><h2>Page found but there is no content :P</h2></center>')


def rm_user(request):
    try:
        TempURL.objects.all().delete()
        TempUser.objects.all().delete()
        ret = 'user objects deleted!'
    except Exception as ret:
        pass
    print(ret)
    return HttpResponse(ret)


def verify(request, username, verify_code):
    def move_data():
        registeredUser = RegisteredUser(username=username,
                                        user_email=tempUser.get(id=tempUserID).user_email,
                                        user_password=tempUser.get(id=tempUserID).user_password)

    def verify_credentials():
        if verify_code == db_verify_code:
            print('Entered verify code equals verify code from database...\n'
                  'Moving TempUser to Registered User!')
            try:
                tempURL.get(id=tempURL_id).delete()
                tempUser.get(id=tempUser_id).delete()
                print(f'tempURL and tempUser (tempUser_id: {tempUser_id} / tempURL_id: {tempURL_id}) deleted!')
            except Exception as exp:
                print(f'Could not delete tempURL and tempUser - {exp}')

        else:
            print('Entered verify code does not equal verify')

        print(db_verify_code)

    context = {
        'username': username,
        'verify_code': verify_code
    }

    tempURL = TempURL.objects.all()
    tempUser = TempUser.objects.all()

    try:
        tempURL_id = tempURL.get(username=username).id()
        tempUser_id = tempUser.get(username=username).id()
        db_verify_code = tempURL.get(id=tempURL_id).verification_code()
        verify_credentials()
    except:
        return HttpResponse('Already verified credentials or invalid verification code!')
    return render(request, 'templates/verify.html', context=context)


def register(request):
    def register_user_in_database():
        register_user = TempUser(username=username, user_email=user_email, user_password=user_password)

        """
            - Check data before saving the User in the Database
                - More security coming soon
        """

        print(username)
        print(user_email)
        print(user_password)

        register_user.save()  # SAVE USER IN TEMP DATABASE
        print(f'New User added to database - {register_user}')
        verificationURL, verificationCode = register_user_verification.create_custom_url(username)
        tempURL = TempURL(verification_code=verificationCode, username=username)
        tempURL.save()
        print(verificationURL)
        # Send verificationURL to User

    context = {
        'type': 'register',
        'href': '/login',
        'linkText': 'Already have an Account?'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        user = TempUser.objects.all()
        user_objs_username = user.filter(username=username).first()
        user_objs_email = user.filter(user_email=user_email).first()

        if user_objs_email is None and user_objs_username is None:
            print('verifying user credentials...')
            print("Creating new User...")
            register_user_in_database()
        else:
            print("E-Mail or Username already registered.")


    """
    - - - - - - - - -
    Daten müssten dann wahrscheinlich irgendwie mit JavaScript im Frontend
    verschlüsselt werden, mal sehen, ob ich da eine eigene Hash-Funktion für baue
    - - - - - - - - -
    Ablauf:
        - register
        - Save Data in database
        - send email to EMAIL-ADRESS
        - accept email
            - True: verify data in database
            - False: delete Data after 10 min
    """
    return render(request, 'templates/register.html', context)


def login(request):
    def check_database():
        user = TempUser.objects.all()
        db_username_lookup = user.filter(username=username).first()
        if db_username_lookup is not None:
            user_id = db_username_lookup.id
            db_password_lookup = user.get(id=user_id).user_password
            print(db_password_lookup)
        print(db_username_lookup)
    context = {
        'type': 'login',
        'href': '/register',
        'linkText': 'Don\'t have an Account?'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        user_password = request.POST.get('password')
        check_database()

        print(username)
        print(user_password)
    return render(request, 'templates/login.html', context)
