from django.urls import path
from .views import evaluate_view
from lEvaluation.views import index

urlpatterns = [
    path('evaluate/<int:staff_id>/<int:course_id>/<int:semester_id>/', evaluate_view, name='evaluate'),

]
