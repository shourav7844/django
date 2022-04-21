from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import registration
from django.contrib.auth.models import User, auth
from . import models

# Create your views here.

def home(request):
    return render(request, 'firstPage.html')

def save(request):
    if request.method == "POST":
        name = request.POST.get('NAME')
        email = request.POST.get('EMAIL')
        password = request.POST.get('PASSWORD')
        InsertInDatabaseVariable = registration(Name = name, Email_address = email, Password = password)
        InsertInDatabaseVariable.save()
    else:
        return render(request, 'register/form.html')
    return render(request, 'register/form.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        password = request.POST.get('PASSWORD')

        user = auth.authenticate(Email_address = email, Password = password)
        if user in models.registration:
            auth.login(request, registration)
            return redirect('login/login')
        else:
            return HttpResponse('Invalid')

    else:
        return render(request, 'login/login.html')

def thankyou(request):
    return render(request, 'register/thankyou.html')

def firstPage(request):
    return render(request, 'firstPage.html')
    