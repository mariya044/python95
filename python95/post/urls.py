from . import views
from django.urls import path, include
from post.views import PostDeleteView


urlpatterns = [
    path("posts/", views.posts, name="posts"),
    path('posts/<int:post_id>/', views.posts_view, name="posts"),
    path("create/", views.create, name="create"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("<int:pk>/delete",PostDeleteView.as_view(), name="post_delete"),
]




