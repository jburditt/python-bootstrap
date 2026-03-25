from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.http import JsonResponse
from .models import User
from .repository import UserRepository
from datetime import date

Repository = UserRepository(User.objects)

def search(request, username, email):
    users = []
    if username == "email":
        username = None
    if username or email:
        # Search for users where username or email contains the query string
        users = list(User.objects.filter(
            Q(username__icontains=username) | Q(email__icontains=email)
        ).distinct().values())
    return JsonResponse(users, safe=False)

def create_sample_user(request):
    user = Repository.create_user(
        username="john_doe",
        email="john.doe@example.com",
        first_name="John",
        last_name="Doe",
        role=1
    )
    return JsonResponse({"id": user.id, "username": user.username})

def list_users(request):
    users = Repository.get_all_users()
    return JsonResponse({"users": [{"id": u.id, "username": u.username} for u in users]})
