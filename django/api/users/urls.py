from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("list/", views.list_users, name="list_users"),
    path("create/", views.create_sample_user, name="create_sample_user"),
    path("<str:username>/", views.search, name="search"),
    path("email/<str:email>/", views.search, name="search"),
    path("<str:username>/<str:email>/", views.search, name="search"),
]