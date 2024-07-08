from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from post.models import Post

admin.site.register(Post)
