from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
# # Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=10, blank=True)
    last_name = models.CharField(_("last name"), max_length=10, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    # User Manager here
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name.strip()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50,blank=True)
    province = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.get_full_name()




    