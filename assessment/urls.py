from django.urls import path
from .views import evaluate_view, add_answers_view, lecturer_result_view
from lEvaluation.views import index

urlpatterns = [
    path('add-answer/<int:assessment_id>/', add_answers_view, name='add_answers'),
    path('evaluate/<int:staff_id>/<int:course_id>/<int:semester_id>/', evaluate_view, name='evaluate'),
    path('lecturer/result/<course_id>/<semester_id>/<lecturer_id>', lecturer_result_view, name="lecturer_result_view")
    # path('add-answer/', add_answers_view, 'add_answers'),
]
