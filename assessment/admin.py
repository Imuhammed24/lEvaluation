from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from assessment.models import Semester, Assessment, Question, Answer


@admin.register(Semester)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name', 'year']


@admin.register(Assessment)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name', 'lecturer', 'course', 'semester']


@admin.register(Question)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['question_text', 'is_published', 'exam']


@admin.register(Answer)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['text', 'question', 'student']
