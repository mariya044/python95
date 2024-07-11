from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_request, name='login'),
    path('account/',views.account,name='account'),
    path('logout/',views.custom_logout,name='logout')
]