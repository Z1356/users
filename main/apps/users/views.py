from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

def index(request):
    if "users" not in request.session:
        request.session["users"] = []
    print request.session["users"]
    context = {
        "users":User.objects.all(),
        "id":id
    }
    return render(request, 'users/users.html', context)

def user(request, id):
    context = {
        "users":User.objects.all(),
        "id":id
    }
    return render(request, 'users/user.html', context)

def edit(request, id):
    context = {
        "users":User.objects.all(),
        "id":id
    }
    return render(request, 'users/edit.html', context)

def new(request):
    if "users" not in request.session:
        request.session["users"] = []
    if request.method == "POST":
        User.objects.create(
            first=request.POST["first"], 
            last=request.POST["last"], 
            email=request.POST["email"]
        )
        return redirect('/users/')
    return render(request, 'users/new.html')