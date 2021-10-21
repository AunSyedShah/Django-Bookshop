from django.urls import path
from account.views import register
from django.contrib.auth import views as auth_views

from account.forms import CustomAuthForm, CustomPasswordResetForm
urlpatterns = [
    path("account/register/", register, name="register"),
    path('account/login/',
        auth_views.LoginView.as_view(template_name="account/login.html", authentication_form = CustomAuthForm),
        name="login",
        ),
    path('password-reset', 
        auth_views.PasswordResetView.as_view(template_name="account/password-reset.html", form_class = CustomPasswordResetForm),
        name="password-reset-request"),

    path("account/logout/", auth_views.LogoutView.as_view(),name="logout"),
    
    
]