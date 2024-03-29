from django.contrib import admin
from account.models import Profile, ExtraCourses, AssessedCourses
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin, User


class ProfileInline(admin.TabularInline):
    model = Profile
    raw_id_fields = ['user']


class UserAdmin(AuthUserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser']
    inlines = [ProfileInline]


# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)

admin.site.register(Profile)

admin.site.register(ExtraCourses)

admin.site.register(AssessedCourses)
