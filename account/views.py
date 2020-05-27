from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import LoginForm


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
    return render(request, 'account/dashboard.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login_view')
