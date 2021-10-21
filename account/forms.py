from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.forms.widgets import EmailInput, PasswordInput
from account.models import User, Profile
from django import forms
from django.utils.translation import gettext_lazy as _
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email","first_name","last_name","password1","password2"]
    
    def __init__(self, *args, **kwargs) -> None:
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs["placeholder"] = self.fields[key].label
            self.fields[key].widget.attrs["id"] = self.fields[key].label



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["province","city","country","address", "phone_number"]

    def __init__(self, *args, **kwargs) -> None:
        super(UserProfileForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs["placeholder"] = self.fields[key].label
            self.fields[key].widget.attrs["id"] = self.fields[key].label


class CustomAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["email","password"]


    def __init__(self, request, *args, **kwargs) -> None:
        super(CustomAuthForm, self).__init__(request=request, *args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs["placeholder"] = self.fields[key].label
            self.fields[key].widget.attrs["id"] = self.fields[key].label


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email',"id":"email","placeholder":"Email"})
    )
