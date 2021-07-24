from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("news/<int:post_id>/", views.news, name="news"),
]
