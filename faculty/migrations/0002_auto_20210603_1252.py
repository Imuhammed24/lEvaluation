# Generated by Django 3.2 on 2021-06-03 12:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lecturer',
        ),
        migrations.AddField(
            model_name='course',
            name='lecturer',
            field=models.ManyToManyField(limit_choices_to={'is_staff': True}, null=True, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
