from django.urls import path
from . import views

urlpatterns = [
    path("", views.personal_info, name="personal_info"),
]