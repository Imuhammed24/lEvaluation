from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from assessment.models import Assessment
from faculty.models import Department, Course


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
    department = models.ForeignKey(Department, blank=True, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(choices=LEVEL, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


class ExtraCourses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extra_courses')
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.user}: extra course'


class AssessedCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessed_courses')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='assessed_students')

    def __str__(self):
        return f'{self.user}: >>> {self.assessment.course}'
