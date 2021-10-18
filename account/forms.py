from django.contrib.auth.forms import UserCreationForm
from account.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email","first_name","last_name","password1","password2"]
    
    def __init__(self, *args, **kwargs) -> None:
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            self.fields[key].widget.attrs["placeholder"] = self.fields[key].label
            self.fields[key].widget.attrs["id"] = self.fields[key].label



