from app.models import RegisteredUser
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse


def main_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('accounts/login')
    user = RegisteredUser.objects.all().get(id=user_id)
    username = user.username
    if request.method == 'POST':
        request.session.flush()
        return redirect('accounts/login')

    context = {
        'username': username
    }

    return render(request, 'templates/mainAppTemplates/main.html', context=context)
