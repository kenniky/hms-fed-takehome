from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def class_view(request, class_slug):
    return render(request, "class.html", context={'class_slug': class_slug})