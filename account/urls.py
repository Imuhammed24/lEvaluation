from django.urls import path
from .views import login_view, account_view, logout_view
from django.contrib.auth import views as auth_views
from lEvaluation.views import index

urlpatterns = [
    path('', login_view, name='login_user'),
    path('login/', index, name='login_view'),
    path('profile/', account_view, name='profile'),
    path('logout/', logout_view, name='logout'),

]
