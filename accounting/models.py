from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Gender = (
        ('f', 'female'),
        ('m', 'male')
    )
    user_image = models.ImageField(upload_to='media\ user_image', null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True,
        null=True
    )
    USERNAME_FIELD = 'username'
    PhoneNumber = models.CharField(max_length=12, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    created_day = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=Gender, default='male')
