from django.conf import settings
from django.db import models

# Create your models here.
from faculty.models import Department


class Profile(models.Model):

    # DEPARTMENTS = (
    #     ('cyber security science', 'Cyber Security Science'),
    #     ('computer science', 'Computer Science'),
    #     ('information and media technology', 'Information and Media Technology'),
    # )
    LEVEL = (
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    department = models.ManyToManyField(Department, blank=True)
    level = models.IntegerField(choices=LEVEL, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return f'{self.user.username}'
