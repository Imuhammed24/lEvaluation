from django.contrib.auth.models import User
from django.db import models

from faculty.models import Course

SEMESTER = (
    ('FIRST SEMESTER', 'FIRST SEMESTER'),
    ('SECOND SEMESTER', 'SECOND SEMESTER')
)

class Semester(models.Model):
    name = models.CharField(max_length=20, choices=SEMESTER)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.year}'


class Assessment(models.Model):
    """
    Assessment's model, works as a wrapper for the questions
    """
    lecturer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='students_assessments',
                                 limit_choices_to={'is_staff': True})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)


    def __str__(self):
        return f'({self.lecturer.first_name} {self.lecturer.last_name}: {self.course})'


class Question(models.Model):
    question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text')
    is_published = models.BooleanField(default=False)
    exam = models.ForeignKey(Assessment, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return "{content} - {published}".format(content=self.question_text[:15], published=self.is_published)


class Answer(models.Model):
    """
    Answer's Model, which is used as the answer in Question Model
    """
    text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
    is_valid = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessment_answers')

    def __str__(self):
        return self.text
