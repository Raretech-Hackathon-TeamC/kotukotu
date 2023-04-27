from django.db import models
from django.urls import reverse_lazy

from django.contrib.auth.models import (
    AbstractBaseUser,PermissionsMixin, UserManager
)

class Users(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=255, unique=True, error_messages={
            "unique": "このメールアドレスは既に使用されています。",
        },)
    token = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('kotukotu:home')
