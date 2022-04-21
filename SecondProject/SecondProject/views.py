from django.http import HttpResponse
from django.shortcuts import render

#Create views here
def index(request):
    return render(request, 'homePage.html')
