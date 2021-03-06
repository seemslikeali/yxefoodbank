from re import L
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password=None,):
        # in case fields are left empty
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first_name')
        if not last_name:
            raise ValueError('Users must have a last_name')
        if not phone:
            raise ValueError('Users must have a phone number')

        # a base for user creations. this is require information to be filled for a regular account
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # super user is required to create staff => is_staff
    def create_superuser(self, email, username, password, first_name, last_name, phone):
        user = self.create_user(
            username=username,
            password=password,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# account creation restrictions and sql fields
class Account(AbstractBaseUser):
    # data fields, some are generated and some are asked user
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(verbose_name="phone", max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    # can add more required fields here
    REQUIRED_FIELDS = ['email', 'phone', 'first_name', 'last_name']
    # uses account MyAccountManager to go through each option require to create user
    objects = MyAccountManager()

    # Django requirements, account creation doesn't work without these fields as per documentations
    def __str__(self):
        # kind of like a 'to string' method
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
