from django.urls import path
from . import views

app_name = "lessons"
urlpatterns = [
    path("sequences/", views.LessonViews.sequences, name="sequences"),
    path("tuples/", views.LessonViews.tuples, name="tuples"),
    path("ranges/", views.LessonViews.ranges, name="ranges"),
    path("language/", views.LessonViews.language_reference, name="language_reference"),]