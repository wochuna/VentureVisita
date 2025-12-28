from django.db import models
from django.utils import timezone

class User(models.Model):
    USER_ROLES = [
        ('customer', 'Customer'),
        ('provider', 'Hike Provider'),
    ]
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50, choices=USER_ROLES)
    date_joined = models.DateTimeField(auto_now_add=True)

class AuthToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username
