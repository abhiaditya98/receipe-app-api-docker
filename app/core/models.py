from django.db import models  # noqa
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_field):
        """Create,save and return a new user"""
        # user=self.model(email=email,**extra_field)
        user=self.model(email=self.normalize_email(email.lower()),**extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    """User in System"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
