from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from account.forms import UserRegisterForm, UserProfileForm
# Create your views here.


def register(request):
    register_form = UserRegisterForm()
    profile_form = UserProfileForm()
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if register_form.is_valid() and profile_form.is_valid():
            user = register_form.save()
            profile_form.instance = user.profile
            profile_form.save()
            user.save()
            messages.success(request,f"Account successfuly created for {user.email}.")
            return HttpResponse("User Created")
    context = {
        "title": "Register - Bookshop",
        "reg_form": register_form,
        "pro_form": profile_form
    }
    return render(request, "account/register.html", context=context)