#import Q from django.db.models

from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def search(request, username, email):
    query = request.GET.get('q')
    users = []
    if query:
        # Search for users where username or email contains the query string
        # users = User.objects.filter(
        #     Q(username__icontains=query) | Q(email__icontains=query)
        # ).distinct()
        users = []
    return render(request, 'search_user.html', {'users': users, 'query': query})
