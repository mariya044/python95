from . import views
from django.urls import path
from post.views import PostDeleteView

app_name='post'

urlpatterns = [
    path("posts/", views.posts, name="posts"),
    path('posts/<int:post_id>/', views.posts_view, name="posts"),
    path("create/", views.create, name="create"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("<int:pk>/delete",PostDeleteView.as_view(), name="post_delete"),
    path('subject<int:subject_id>/',views.posts,name='subject'),
    path('post_comment/<int:post_id>/', views.post_comment, name='post_comment'),
]




