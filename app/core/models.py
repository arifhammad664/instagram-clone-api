"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, user_name=None, **extra_fields):
        """Create, save and return a new user."""
        if not user_name:
            user_name = email.split('@')[0]

        if not email:
            raise ValueError('user must have an email address.')

        user = self.model(email=self.normalize_email(email), user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return and new super user."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    objects = UserManager()

    USERNAME_FIELD = 'email'
