from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
# my User Manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,email,password, is_staff, is_superuser,**extra_fields):
        """
        Create and save user
        """
        if not email:
            raise ValueError("Email is not available")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email, password=None, **extra_fields):
        """
        Create a user
        """

        return self._create_user(email, password, False, False,**extra_fields)
    
    def create_superuser(self,email, password, **extra_fields):
        """
        Create super user 
        """
        return self._create_user(email, password,True, True,**extra_fields)


