from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    department = models.DateField(blank=True, null=True)
    level = models.IntegerField(blank=True)

    def __str__(self):
        return f'profile for user {self.user.username}'
