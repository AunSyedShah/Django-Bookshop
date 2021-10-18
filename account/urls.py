from django.urls import path
from account.views import register

urlpatterns = [
    path("account/register/", register, name="register")
]