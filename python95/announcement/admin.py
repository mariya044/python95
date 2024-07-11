from django.contrib import admin
from announcement.models import Announcement, Subject


class AnnouncementAdmin(admin.ModelAdmin):
    fields = ['first_name', "subject"]


admin.site.register(Announcement, AnnouncementAdmin)


class SubjectAdmin(admin.ModelAdmin):
    fields = ['subject']


admin.site.register(Subject, SubjectAdmin)
