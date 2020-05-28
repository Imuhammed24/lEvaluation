from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)
    lecturers = models.ManyToManyField(User, related_name='department', blank=True, limit_choices_to={'is_staff': True})

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):

    LEVEL = (
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500'),
    )

    title = models.CharField(max_length=30)
    lecturer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='courses',
                                 limit_choices_to={'is_staff': True})
    departments_offering = models.ManyToManyField(Department, blank=True, related_name='courses')
    level_offering = models.IntegerField(choices=LEVEL, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Faculty(models.Model):
    name = models.CharField(max_length=40)
    departments = models.ManyToManyField(Department, blank=True, related_name='faculty')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Faculties'
