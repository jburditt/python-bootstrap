from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("list/", views.UserViews.list_users, name="list_users"),
    path("create/", views.UserViews.create_sample_user, name="create_sample_user"),
    path("get/<int:user_id>/", views.UserViews.get_user, name="get_user"),
    path("update/", views.UserViews.update_user, name="update_user"),
    path("<str:username>/", views.UserViews.search, name="search"),
    path("email/<str:email>/", views.UserViews.search, name="search"),
    path("<str:username>/<str:email>/", views.UserViews.search, name="search"),
]