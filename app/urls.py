from django.urls import path
from . import views

urlpatterns = [
    # QUICK REMOVE DATA FROM DATABASE | START
    path('rm-user/', views.rm_user),
    # QUICK REMOVE DATA FROM DATABASE | END
    path('register/', views.register),
    path('login/', views.login),
    path('', views.main),
]
