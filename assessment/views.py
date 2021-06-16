from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from account.models import AssessedCourses
from assessment.models import Semester, Assessment, Question, Answer
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


def add_answers_view(request, assessment_id):
    assessment = Assessment.objects.get(id=assessment_id)
    if request.method == 'POST':
        for count, item in enumerate(request.POST):
            if count > 0:
                question_id = item
                question = Question.objects.get(id=question_id, course=assessment)
                answer = Answer(text=request.POST.get(item), question=question, student=request.user)
                answer.save()
                confirm_assessment = AssessedCourses(user=request.user, assessment=assessment)
                confirm_assessment.save()
            if count > 14:
                messages.success(request, "Response Added Successfully!")
    return redirect('account:home')


def lecturer_result_view(request, course_id, semester_id, lecturer_id):
    course = Course.objects.get(id=course_id)
    semester = CurrentSemester.objects.get(id=semester_id)
    lecturer = User.objects.get(id=lecturer_id)
    real_semester = Semester.objects.get(name=semester.name, year=semester.year)
    if Assessment.objects.filter(lecturer=lecturer, course=course, semester=real_semester).count() > 0:
        assessment = Assessment.objects.get(lecturer=lecturer, course=course, semester=real_semester)
    else:
        messages.error(request, 'no assessment uploaded for lecturer yet')
        return redirect('account:home')
    questions = Question.objects.filter(course=assessment)

    context = {
        'section': 'lecturer_result_view',
        'course': course,
        'questions': questions,
        'assessment': assessment,
        'lecturer': lecturer,
    }
    return render(request, 'assessment/lecturer_assessment_result.html', context=context)
