from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'login.html')

def register(request):
    errors = User.objects.registerValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    newuser = User.objects.create(name = request.POST['name'], username = request.POST['username'])
    request.session['loggedinId'] = newuser.id
    return redirect('/home')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.get(username = request.POST['username'])
    request.session['loggedinId'] = user.id
    return redirect('/home')

def home(request):
    return render(request, 'home.html')
