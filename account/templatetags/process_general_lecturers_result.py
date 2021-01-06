# process_general_lecturers_result
from django import template

from assessment.models import Semester, Assessment

register = template.Library()


@register.simple_tag()
def get_lecturer_performance(course, semester):
    assessment_semester = Semester.objects.get(name=semester.name, year=semester.year)
    assessment = Assessment.objects.get(course=course, semester=assessment_semester, lecturer=course.lecturer)
    questions = assessment.questions.all()
    return f'{course.id}'
