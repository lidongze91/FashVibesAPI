from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None, bio="", web="", full_name=""):
        """creates a new user profile project."""

        if not email:
            raise ValueError("User must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, bio=bio, web=web, full_name=full_name)

        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self, email, name, password):
        """creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a 'user profile' inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=1000, blank=True, default='')
    web = models.CharField(max_length=255, blank=True, default='')
    full_name = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name."""

        return self.name


    def get_short_name(self):
        """Used to get a user's short name."""

        return self.name


    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""

        return self.email

