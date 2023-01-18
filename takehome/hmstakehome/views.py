from django.shortcuts import render
from django.http import HttpResponse
from .models import Class

# Create your views here.
def home(request):
    return render(request, "home.html")

def class_selector(request):
    courses = Class.objects.all()

    # times might not be in order, so sort them
    for course in courses:
        course.times.sort(key=lambda time: (time['day'], time['starttime']))

        for time in course.times:
            # create human-readable day field
            if time['day'] == 1:
                time['day_human_readable'] = 'M'
            elif time['day'] == 2:
                time['day_human_readable'] = 'Tu'
            elif time['day'] == 3:
                time['day_human_readable'] = 'W'
            elif time['day'] == 4:
                time['day_human_readable'] = 'Th'
            elif time['day'] == 5:
                time['day_human_readable'] = 'F'
            else:
                time['day_human_readable'] = '?'

            # create human-readable time fields
            time['starttime_human_readable'] = '{}:{:02d}'.format(time['starttime'] // 60, time['starttime'] % 60)
            time['endtime_human_readable'] = '{}:{:02d}'.format(time['endtime'] // 60, time['endtime'] % 60)

    return render(request, "class_selector.html", context={'courses': courses})

def class_selector_submit(request):
    return HttpResponse('hello')