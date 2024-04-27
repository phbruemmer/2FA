from django.shortcuts import render, HttpResponse
from .models import User


def main(request):
    return HttpResponse('<center><h1>404</h1><br><h2>Page found but there is no content :P</h2></center>')


def rm_user(request):
    try:
        User.objects.all().delete()
        ret = 'user objects deleted!'
    except Exception as ret:
        pass
    print(ret)
    return HttpResponse(ret)


def register(request):
    def register_user_in_database():
        register_user = User(username=username, user_email=user_email, user_password=user_password)

        """
            - Check data before saving the User in the Database
                - More security coming soon
        """

        print(username)
        print(user_email)
        print(user_password)

        register_user.save()  # SAVE USER IN DATABASE
        print(f'New User added to database - {register_user}')

    context = {
        'type': 'register',
        'href': '/login',
        'linkText': 'Already have an Account?'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        user = User.objects.all()
        user_objs_username = user.filter(username=username).first()
        user_objs_email = user.filter(user_email=user_email).first()

        if user_objs_email is None and user_objs_username is None:
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
        user = User.objects.all()
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
