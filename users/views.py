from django.shortcuts import render
from storage import load_users


def user_list(request):
    users = load_users("data/users.json")
    context = {
        "users": users,
    }
    return render(request, "users/user_list.html", context)
