from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # superuser作成用
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True, error_messages={
            "unique": "このメールアドレスは既に使用されています。",
        },)
    token = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 

    # userクラスのレコードを一意に識別するのがemailです。
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('activity:home')
