from django import forms

from announcement.models import Announcement


class StudentAnnouncementForm(forms.ModelForm):
    class Meta:
        model=Announcement
        fields=("first_name","form","age","city","address","price_limit_from","price_limit_to","currency","online_lessons",
                "offline_lessons",
                "lessons_at_home","level_of_knowledge","phone_number","subject")


