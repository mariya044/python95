from django import forms
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("image","first_name","second_name",
                  "subject",
                  "about",
                  "qualification",
                  "work_experience",
                  "organizations",
                  "address",
                  "online_lessons",
                  "offline_lessons",
                  "lessons_at_home",
                  "price",
                  "currency",
                  "time_of_lesson",
                  "add_information",)



