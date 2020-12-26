from django.http import HttpResponse
from django.shortcuts import render
from account.forms import LoginForm


def index(request):
    form = LoginForm()
    return render(request, 'index.html', {
        'html_title': 'Welcome to L-evaluation Portal',
        'login_form': form, })
