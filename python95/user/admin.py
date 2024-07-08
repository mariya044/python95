from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from user.models import NewUser



admin.site.register(NewUser, UserAdmin)


