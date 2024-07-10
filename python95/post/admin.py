from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['first_name', 'subject']


admin.site.register(Post, PostAdmin)
