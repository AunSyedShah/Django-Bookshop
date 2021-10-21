from django.urls import path
from account.views import register
from django.contrib.auth import views as auth_views

from account.forms import CustomAuthForm, CustomPasswordResetForm, CustomSetPaswordForm
urlpatterns = [
    path("account/register/", register, name="register"),
    path('account/login/',
        auth_views.LoginView.as_view(template_name="account/login.html", authentication_form = CustomAuthForm),
        name="login",
        ),
    path('password-reset', 
        auth_views.PasswordResetView.as_view(template_name="account/password-reset.html", form_class = CustomPasswordResetForm),
        name="password-reset-request"),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="account/password-reset-done.html"),
        name="password_reset_done"),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="account/password-reset-confirm.html", form_class=CustomSetPaswordForm),
        name="password_reset_confirm"),
    
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name = 'account/password-reset-complete.html'),
        name="password_reset_complete"),

    path("account/logout/", auth_views.LogoutView.as_view(),name="logout"),
    
    
]