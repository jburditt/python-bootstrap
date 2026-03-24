from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("<str:username>/", views.search, name="search"),
    path("email/<str:email>/", views.search, name="search"),
    path("<str:username>/<str:email>/", views.search, name="search"),
]