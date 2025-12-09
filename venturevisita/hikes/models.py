from django.db import models
from users.models import User

class Hike(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hikes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title