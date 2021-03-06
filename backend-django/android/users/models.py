from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, first_name, password, **other_fields)

    def create_user(self, username, first_name, password, **other_fields):

        # if not email:
        #     raise ValueError(_('You must provide an email address'))

        # email = self.normalize_email(email)
        user = self.model(username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), blank=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    major = models.CharField(max_length=150, blank=True)
    bio = models.CharField(max_length=150,blank=True)
    is_in = models.CharField(max_length=50, blank=True)
    applied = models.JSONField(default=list)
    role = models.CharField(max_length=150,blank=True)
    likes = models.JSONField(default=list)
    objects = CustomAccountManager()
    isTeacher = models.BooleanField(default=False)
    # USERNAME_FIELD = 'email'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.username