from django.shortcuts import render
from . import views

# Create your views here.

def index(requests):
    return render(request, 'views/index.html')