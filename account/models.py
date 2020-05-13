from django.conf import settings
from django.db import models

# Create your models here.
from faculty.models import Department


class Profile(models.Model):

    DEPARTMENTS = (
        ('cyber security science', 'Cyber Security Science'),
        ('computer science', 'Computer Science'),
        ('information and media technology', 'Information and Media Technology'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    # department = models.CharField(max_length=40, choices=DEPARTMENTS, null=True, blank=True)
    department = models.OneToOneField(Department, on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'
