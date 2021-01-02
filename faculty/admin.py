from django.contrib import admin

# Register your models here.
from faculty.models import Faculty, Department, Course, CurrentSemester


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CurrentSemester)
