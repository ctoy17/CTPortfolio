from django.shortcuts import render
from django.http import HttpResponse

import logging
logging.basicConfig(level=logging.DEBUG)
# Create your views here.

def home(request):
    """
    home view
    http://localhost:8000/
    """
    return render(request, 'home.html')


def projects(request):
    """
    about view
    http://localhost:8000/projects/
    """
    return render(request, 'projects.html')