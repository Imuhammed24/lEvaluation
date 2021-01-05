from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import LoginForm
from account.models import Profile
from faculty.models import Course


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if not user:
                user = authenticate(username=cd['username'].title(), password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account:home')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    return HttpResponse('No post')

#
# @login_required
# def account_view(request):
#     context = {
#         'display_section': 'dashboard',
#                }
#     return render(request, 'account_base.html', context)
#


@login_required
def home_view(request):
    assessed_courses = []
    context = {
        'display_section': 'Dashboard',
        'assessed_courses': assessed_courses,
    }
    # test = Course.objects.get(level_offering=500)
    # print([test.name for test in test.departments_offering.all()])
    for assessment in request.user.assessed_courses.all():
        assessed_courses.append(assessment.assessment.course)

    if not request.user.is_staff:
        # user_profile = Profile.objects.get(user=request.user)
        courses = Course.objects.filter(departments_offering__in=[request.user.profile.department],
                                        level_offering=request.user.profile.level)
        context['courses'] = courses
    else:
        courses = request.user.courses.all()
        context['courses'] = courses

    if request.user.is_superuser:
        template = 'account/dashboards/admin_dashboard.html'
    elif request.user.is_staff:
        template = 'account/dashboards/staff_dashboard.html'
    else:
        template = 'account/dashboards/student_dashboard.html'

    return render(request, template, context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login_view')
