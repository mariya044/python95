from django.urls import path, include
from . import views
from .views import AnnouncementDeleteView

app_name = 'announcement'

urlpatterns = [
    path("create_announcement/", views.add_announcement, name="create_announcement"),
    path("announcements/", views.announcement, name="announcements"),
    path("edit_announcement/<int:announcement_id>/", views.edit_announcement, name="edit_announcement"),
    path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement'),
    path("<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="delete_announcement"),
    path("subject<int:subject_id>/", views.announcement, name='subject'),

]
