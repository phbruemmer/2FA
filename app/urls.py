from django.urls import path, include
from . import views

urlpatterns = [
    # QUICK REMOVE DATA FROM DATABASE | START
    path('rm-user/', views.rm_user),
    # QUICK REMOVE DATA FROM DATABASE | END
    path('register/', views.register),
    path(r'verify/<str:username>/<str:verify_code>/', views.verify),
    path('login/', views.login),
    path(r'login/verify_code/<str:username>/', views.handle_login_code, name='handle_login_code'),
    path(r'login/reset_password/', views.reset_password, name='reset_password'),
    path(r'recover/<str:user_id>/<str:code>/', views.change_password, name='change_password')
]
