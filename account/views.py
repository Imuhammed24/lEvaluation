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
    context = {
        'display_section': 'Dashboard',
    }
    # test = Course.objects.get(level_offering=500)
    # print([test.name for test in test.departments_offering.all()])
    if not request.user.is_staff:
        # user_profile = Profile.objects.get(user=request.user)
        courses = Course.objects.filter(departments_offering__in=request.user.profile.department.all(),
                                        level_offering=request.user.profile.level)
        context['courses'] = courses

    return render(request, 'account/dashboard.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login_view')
