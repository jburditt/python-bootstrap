from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

def search(request, username, email):
    users = []
    if username and email:
        # Search for users where username or email contains the query string
        users = User.objects.filter(
            Q(username__icontains=username) | Q(email__icontains=email)
        ).distinct()
        users = []
    return JsonResponse(users, safe=False)
