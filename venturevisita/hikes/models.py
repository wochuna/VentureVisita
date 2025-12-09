from django.db import models
from users.models import User
from django.utils import timezone


class Hike(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    location = models.CharField(max_length=200)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hikes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    