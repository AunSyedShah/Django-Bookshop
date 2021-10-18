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







# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=254, unique=True)
#     name = models.CharField(max_length=254, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
    

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def get_absolute_url(self):
#         return "/users/%i/" % (self.pk)