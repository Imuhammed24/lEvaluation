from django.contrib.auth.models import User
from django.shortcuts import render

from assessment.models import Semester, Assessment
from faculty.models import Course, CurrentSemester


def evaluate_view(request, staff_id, course_id, semester_id):
    staff = User.objects.get(id=staff_id)
    course = Course.objects.get(id=course_id)
    semester = CurrentSemester.objects.get(id=semester_id)
    real_semester = Semester.objects.get(name=semester.name, year=semester.year)
    assessment = Assessment.objects.get(lecturer=staff, course=course, semester=real_semester)
    context = {
        'section': 'assessment',
        'assessment': assessment,
    }
    return render(request, 'assessment/assessment.html', context)
