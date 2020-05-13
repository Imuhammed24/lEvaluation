from django.contrib import admin
from account.models import Profile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin, User


class ProfileInline(admin.TabularInline):
    model = Profile
    raw_id_fields = ['user']


class UserAdmin(AuthUserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]


# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)

admin.site.register(Profile)
