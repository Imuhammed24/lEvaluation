from django import template

from assessment.models import Assessment

register = template.Library()


@register.simple_tag()
def check_assessed_status(user, course, lecturer, semester):
    print(semester)
    assessment = Assessment.objects.filter(course=course,
                                           lecturer=lecturer,
                                           semester=semester).first()
    if user.assessed_courses.filter(user=user, assessment=assessment).count() > 0:
        return '(Evaluated)'
    else:
        return ''
    # pass


@register.simple_tag()
def check_assessed_status_for_disable(user, course, lecturer, semester):
    print(semester)
    assessment = Assessment.objects.filter(course=course,
                                           lecturer=lecturer,
                                           semester=semester).first()
    if user.assessed_courses.filter(user=user, assessment=assessment).count() > 0:
        return 'disabled'
    else:
        return ''
    # pass
