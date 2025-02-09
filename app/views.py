from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .libraries import register_user_verification, send_email_templates, check
from .libraries import hash_function as hf
from .models import *


def change_password(request, user_id, code):
    context = {
        'type': 'Reset Password',
        'href': '/login/../../',
        'linkText': 'Back to login',
    }
    temp_code_data = get_object_or_404(TempResetCode, user_id=user_id)

    if temp_code_data.reset_code != code:
        messages.error(request, "Invalid or expired reset code.")
        return redirect('login')

    if request.method == 'POST':
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            messages.error(request, "Passwords do not match.")
        elif not check.check_password(password_1):
            messages.error(request, "Password does not meet criteria.")
        else:
            hashed_password = hf.sha256(password_1)
            user_data = get_object_or_404(RegisteredUser, id=user_id)
            user_data.user_password = hashed_password
            user_data.save()

            temp_code_data.delete()

            return redirect(login)

    return render(request, 'templates/change_password.html', context=context)


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user_id = RegisteredUser.objects.all().get(user_email=email).id
            url, code = register_user_verification.create_recovery_code(user_id)
            temp_reset = TempResetCode.objects.all()
            if temp_reset.filter(user_id=user_id):
                temp_reset.filter(user_id=user_id).delete()
            temp_recovery_data = TempResetCode(reset_code=code, user_id=user_id)
            temp_recovery_data.save()
            send_email_templates.send_reset_request(user_id, code)
            return redirect(login)
        except Exception as exp:
            print(exp)

    context = {
        'type': 'Reset Password',
        'href': '../',
        'linkText': 'Back to login',
    }

    return render(request, 'templates/reset_password.html', context=context)


def rm_user(request):
    try:
        TempURL.objects.all().delete()
        TempUser.objects.all().delete()
        RegisteredUser.objects.all().delete()
        TempVerifyCode.objects.all().delete()
        TempResetCode.objects.all().delete()
        ret = 'user objects deleted!'
        print(ret)
    except Exception as ret:
        print(ret)
    return HttpResponse(ret)


def verify(request, username, verify_code):
    def check():
        user_check = RegisteredUser.objects.all()
        user_check_id = user_check.filter(username=username).id
        user = user_check.get(id=user_check_id)
        if user.username == username and user.user_email == tempUser.get(
                id=tempUser_id).user_email and user.user_password == tempUser.get(id=tempUser_id).user_password:
            print('- - - Credentials verified - - -')
        else:
            print('Credential verification error - could not move data!')
            user.delete()

    def move_data():
        registeredUser = RegisteredUser(username=username,
                                        user_email=tempUser.get(id=tempUser_id).user_email,
                                        user_password=tempUser.get(id=tempUser_id).user_password)
        registeredUser.save()
        print('checking data...')
        try:
            check()
        except Exception as exp:
            print(f'checking went wrong - {exp}')
        tempUser.get(id=tempUser_id).delete()

    def verify_credentials():
        if verify_code == db_verify_code:
            print('Entered verify code equals verify code from database...\n'
                  'Moving TempUser to Registered User!')
            try:
                tempURL.get(id=tempURL_id).delete()
                print(f'tempURL (tempURL_id: {tempURL_id}) deleted!')
                move_data()
            except Exception as exp:
                print(f'Could not delete tempURL and / or can not move data - {exp}')

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
        tempURL_id = tempURL.get(username=username).id
        tempUser_id = tempUser.get(username=username).id
        db_verify_code = tempURL.get(id=tempURL_id).verification_code
        verify_credentials()
    except Exception as exp:
        return HttpResponse(f'Already verified credentials or invalid verification code!\n{exp}')
    return render(request, 'templates/verify.html', context=context)


def register(request):
    """
    Important future changes:
        - Put the Password / e-mail / username validation check function in the front-end of the application.
    """

    def register_user_in_database(_user_password):
        new_user_password = hf.sha256(_user_password)
        register_user = TempUser(username=username, user_email=user_email, user_password=new_user_password)

        """
            - Check data before saving the User in the Database
                - More security coming soon
        """

        register_user.save()  # SAVE USER IN TEMP DATABASE
        print(f'New User added to database - {register_user}')
        verificationURL, verificationCode = register_user_verification.create_custom_url(username)
        tempURL = TempURL(verification_code=verificationCode, username=username)
        tempURL.save()
        send_email_templates.send_verification(username, verificationCode)
        print(verificationURL)
        # Send verificationURL to User
    error_msg = "Password must be at least 5 characters long"

    if request.method == 'POST':
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        if check.check_password(user_password):
            user = TempUser.objects.all()
            existing_users = RegisteredUser.objects.all()
            existing_objs_username = existing_users.filter(username=username).first()
            existing_objs_email = existing_users.filter(user_email=user_email).first()
            user_objs_username = user.filter(username=username).first()
            user_objs_email = user.filter(user_email=user_email).first()

            if user_objs_email is None and user_objs_username is None:
                print('No temporary / unverified users found')
                if existing_objs_email is None and existing_objs_username is None:
                    print('verifying user credentials...')
                    print("Creating new User...")
                    register_user_in_database(user_password)
                else:
                    error_msg = "User already registered!"
            else:
                error_msg = "E-Mail or Username not verified."
        else:
            error_msg = ("Invalid password - password must be at least 5 characters, contain digits, punctuation, "
                         "lowercase- and uppercase letters!")
    context = {
        'type': 'register',
        'href': '/accounts/login',
        'linkText': 'Already have an Account?',
        'help_text': error_msg
    }
    return render(request, 'templates/register.html', context)


def login(request):
    def handle_verify_code():
        login_code = register_user_verification.create_code()
        try:
            tempObjects = TempVerifyCode.objects.all()
            tempObjId = tempObjects.get(username=username).id
            TempVerifyCode.objects.get(id=tempObjId).delete()
        except Exception as exp:
            print(f'No older codes found - {exp}')
        tempVerifyCode = TempVerifyCode(login_code=login_code, username=username)
        tempVerifyCode.save()
        print(login_code)
        send_email_templates.send_2FA_code(login_code)
        return redirect(handle_login_code, username=username)

    def check_database():
        user = RegisteredUser.objects.all()
        db_username_lookup = user.filter(username=username).first()
        if db_username_lookup is not None:
            user_id = db_username_lookup.id
            db_password_lookup = user.get(id=user_id).user_password
            if user_password == db_password_lookup:
                return True
    context = {
        'type': 'login',
        'href': '/accounts/register',
        'linkText': 'Don\'t have an Account?'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        user_password = request.POST.get('password')
        user_password = hf.sha256(user_password)
        if check_database():
            return handle_verify_code()
    return render(request, 'templates/login.html', context)


def handle_login_code(request, username):
    try:
        verifyCodeObj = TempVerifyCode.objects.all()
        tempVerifyCodeId = verifyCodeObj.get(username=username).id
    except:
        pass

    def display_tries():
        tries = verifyCodeObj.get(id=tempVerifyCodeId).user_try_count
        print(tries)
        return tries

    def check_database():
        login_no_tries = [False, False]
        tempVerifyCode = verifyCodeObj.get(id=tempVerifyCodeId).login_code
        if tempVerifyCode == verify_code:
            verifyCodeObj.get(id=tempVerifyCodeId).delete()
            login_no_tries[0] = True
        else:
            print('Verify codes doesn\'t match!')
            tries = verifyCodeObj.get(id=tempVerifyCodeId)
            tries.user_try_count -= 1
            tries.save()
            tryInt = tries.user_try_count
            print(tryInt)

            """ DECREMENT TRIES AFTER EVERY FAILED TRY """

            if tryInt <= 0:
                verifyCodeObj.get(id=tempVerifyCodeId).delete()
                print('max tries reached - verify code not valid anymore!')
                login_no_tries[1] = True
        return login_no_tries

    if request.method == 'POST':
        verify_code = request.POST.get('login_code')
        print(verify_code)
        redirect_to_page = check_database()
        if redirect_to_page[0]:
            user_id = RegisteredUser.objects.all().get(username=username).id
            print("Something")
            request.session['user_id'] = user_id
            return redirect('main')
        elif redirect_to_page[1]:
            return redirect(login)

    context = {
        'type': 'verify login',
        'href': '/login',
        'linkText': 'Back to login',
        'tries': display_tries()
    }

    return render(request, 'templates/login_verify.html', context=context)
