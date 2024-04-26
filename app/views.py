from django.shortcuts import render, HttpResponse


def main(request):
    return HttpResponse('<center><h1>404</h1><br><h2>Page found but there is no content :P</h2></center>')


def register(request):
    context = {
        'type': 'register',
        'href': '/login',
        'linkText': 'Alreaady have an Account?'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        print(username)
        print(user_email)
        print(user_password)

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
    context = {
        'type': 'login',
        'href': '/register',
        'linkText': 'Don\'t have an Account?'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        user_password = request.POST.get('password')

        print(username)
        print(user_password)
    return render(request, 'templates/login.html', context)
