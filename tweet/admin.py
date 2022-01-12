from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the username field
    fields = ["username", "password", "email"]
    inlines = [ProfileInline]


# Unregister your models here
admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Tweet)
# admin.site.register(Profile)
