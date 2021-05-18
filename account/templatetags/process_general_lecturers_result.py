# process_general_lecturers_result
from django import template

from assessment.models import Semester, Assessment

register = template.Library()


@register.simple_tag()
def get_lecturer_performance(course, semester):
    strongly_agree_count, agree_count, neutral_count, strongly_disagree_count, disagree_count = 0,0,0,0,0
    total_assessment_count = 0
    performance = None

    assessment_semester = Semester.objects.get(name=semester.name, year=semester.year)
    assessment = Assessment.objects.filter(course=course, semester=assessment_semester, lecturer=course.lecturer).first()
    questions = assessment.questions.all()

    for question in questions:
        for answer in question.answers.all():
            total_assessment_count += 1
            if answer.text == 'Strongly Agree':
                strongly_agree_count += 1
            elif answer.text == 'Agree':
                agree_count += 1
            elif answer.text == 'Neutral':
                neutral_count += 1
            elif answer.text == 'Disagree':
                disagree_count += 1
            elif answer.text == 'Strongly Disagree':
                strongly_disagree_count += 1

    if not total_assessment_count == 0:
        percentage_sa = (strongly_agree_count / total_assessment_count) * 100
        percentage_a = (agree_count / total_assessment_count) * 100
        percentage_n = (neutral_count / total_assessment_count) * 100
        percentage_d = (disagree_count / total_assessment_count) * 100
        percentage_sd = (strongly_disagree_count / total_assessment_count) * 100

        if percentage_sa + percentage_a > percentage_sd + percentage_d:
            performance = 'good'
        elif (percentage_n > percentage_sa+percentage_a) or\
                (percentage_n > percentage_sd + percentage_d) or\
                (percentage_sa + percentage_a == percentage_sd + percentage_d):
            performance = 'neutral'
        else:
            performance = 'poor'

        return performance

    else:
        return 'Not yet assessed'
