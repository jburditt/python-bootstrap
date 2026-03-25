from django.urls import path
from . import views

app_name = "lessons"
urlpatterns = [
    path("sequences/", views.sequences, name="sequences"),
    path("tuples/", views.tuples, name="tuples"),
    path("ranges/", views.ranges, name="ranges"),
]