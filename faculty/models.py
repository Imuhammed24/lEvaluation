from django.contrib.auth.models import User
from django.db import models


LEVEL = (
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500'),
    )

SEMESTER = (
    ('FIRST SEMESTER', 'FIRST SEMESTER'),
    ('SECOND SEMESTER', 'SECOND SEMESTER')
)


class Faculty(models.Model):
    name = models.CharField(max_length=40)
    # departments = models.ManyToManyField(Department, blank=True, related_name='faculty')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Faculties'


class Department(models.Model):
    name = models.CharField(max_length=40)
    lecturers = models.ManyToManyField(User, related_name='department', blank=True, limit_choices_to={'is_staff': True})
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=10, null=True, blank=True)
    lecturer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='courses',
                                 limit_choices_to={'is_staff': True})
    departments_offering = models.ManyToManyField(Department, blank=True, related_name='courses')
    department_owned = models.ForeignKey(Department,
                                         null=True,
                                         blank=True,
                                         on_delete=models.CASCADE,
                                         related_name='department_courses')
    level_offering = models.IntegerField(choices=LEVEL, null=True, blank=True)

    def __str__(self):
        return f'{self.title}({self.code})'


class CurrentSemester(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='current_semester')
    name = models.CharField(max_length=20, choices=SEMESTER)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.year}'
