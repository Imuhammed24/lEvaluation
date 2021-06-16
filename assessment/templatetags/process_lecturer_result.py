# process_lecturer_result

from django import template

register = template.Library()


@register.simple_tag()
def get_sa_count(question):
    answers_list = [answer for answer in question.answers.all() if answer.text == 'Strongly Agree']
    total_answer_count = question.answers.all().count()
    percentage = (len(answers_list)/total_answer_count)*100
    percentage = round(percentage, 2)
    return f'{percentage}%'


@register.simple_tag()
def get_a_count(question):
    answers_list = [answer for answer in question.answers.all() if answer.text == 'Agree' ]
    total_answer_count = question.answers.all().count()
    percentage = (len(answers_list) / total_answer_count) * 100
    percentage = round(percentage, 2)
    return f'{percentage}%'


@register.simple_tag()
def get_n_count(question):
    answers_list = [answer for answer in question.answers.all() if answer.text == 'Neutral' ]
    total_answer_count = question.answers.all().count()
    percentage = (len(answers_list) / total_answer_count) * 100
    percentage = round(percentage, 2)
    return f'{percentage}%'


@register.simple_tag()
def get_d_count(question):
    answers_list = [answer for answer in question.answers.all() if answer.text == 'Disagree' ]
    total_answer_count = question.answers.all().count()
    percentage = (len(answers_list) / total_answer_count) * 100
    percentage = round(percentage, 2)
    return f'{percentage}%'


@register.simple_tag()
def get_sd_count(question):
    answers_list = [answer for answer in question.answers.all() if answer.text == 'Strongly Disagree' ]
    total_answer_count = question.answers.all().count()
    percentage = (len(answers_list) / total_answer_count) * 100
    percentage = round(percentage, 2)
    return f'{percentage}%'


@register.simple_tag()
def get_overall_score(question):
    performance = None
    total_answer_count = question.answers.all().count()

    answers_list_sa = [answer for answer in question.answers.all() if answer.text == 'Strongly Agree' ]
    percentage_sa = (len(answers_list_sa) / total_answer_count) * 100

    answers_list_a = [answer for answer in question.answers.all() if answer.text == 'Agree' ]
    percentage_a = (len(answers_list_a) / total_answer_count) * 100

    answers_list_n = [answer for answer in question.answers.all() if answer.text == 'Neutral' ]
    percentage_n = (len(answers_list_n) / total_answer_count) * 100

    answers_list_d = [answer for answer in question.answers.all() if answer.text == 'Disagree' ]
    percentage_d = (len(answers_list_d) / total_answer_count) * 100

    answers_list_sd = [answer for answer in question.answers.all() if answer.text == 'Strongly Disagree' ]
    percentage_sd = (len(answers_list_sd) / total_answer_count) * 100

    if percentage_sa + percentage_a > percentage_sd + percentage_d:
        performance = 'good'
    elif (percentage_n > percentage_sa+percentage_a) or\
            (percentage_n > percentage_sd + percentage_d) or\
            (percentage_sa + percentage_a == percentage_sd + percentage_d):
        performance = 'neutral'
    else:
        performance = 'poor'

    return performance
