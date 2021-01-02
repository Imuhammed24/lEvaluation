# from django.db import models

# class Exam(models.Model):
#     """
#     Exam's model, works as a wrapper for the questions
#     """
#     name = models.CharField(max_length=64, verbose_name=u'Exam name', )
#     slug = models.SlugField()
#
#     def __str__(self):
#         return self.name
#
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text')
#     is_published = models.BooleanField(default=False)
#     exam = models.ForeignKey(Exam, related_name='questions')
#
#     def __str__(self):
#         return "{content} - {published}".format(content=self.question_text, published=self.is_published)
#
#
# class Answer(models.Model):
#     """
#     Answer's Model, which is used as the answer in Question Model
#     """
#     text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
#     is_valid = models.BooleanField(default=False)
#     question = models.ForeignKey(Question, related_name='answers')
#
#     def __str__(self):
#         return self.text
