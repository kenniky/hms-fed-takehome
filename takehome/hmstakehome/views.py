from django.shortcuts import render
from .models import Class

# Create your views here.
def home(request):
    return render(request, "home.html")

def class_selector(request):
    courses = Class.objects.all()



    return render(request, "class_selector.html", context={'courses': courses})