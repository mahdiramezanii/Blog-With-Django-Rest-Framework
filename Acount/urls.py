from django.urls import path
from . import views
from rest_framework.authtoken import views as create_token

urlpatterns=[
    path("register",views.RegisterView.as_view()),
    path("login",create_token.obtain_auth_token),

]