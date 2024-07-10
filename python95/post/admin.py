from django.contrib import admin
from post.models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    fields = ['first_name', 'subject']


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['name','post']
    list_filter = ['active','created']
    search_fields = ['name','body']