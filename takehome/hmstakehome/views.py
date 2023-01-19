from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Class, ClassSlate
from .func import prepare_for_display

# Create your views here.
def home(request):
    return render(request, "home.html")

def class_selector(request):
    courses = Class.objects.all()

    for course in courses:
        prepare_for_display(course)

    return render(request, "class_selector.html", context={'courses': courses})

def class_selector_submit(request, learner):
    classes = []

    for key, val in request.POST.items():
        if key[0:7] == 'course-' and val == 'on':
            classes.append(key[7:])

    class_slate = ClassSlate(learner=learner, classes=classes)
    class_slate.save()

    return HttpResponseRedirect(reverse('app:class-selector-result', args=(learner, )))

def class_selector_result(request, learner):
    obj_results = ClassSlate.objects.filter(learner__exact=learner)

    # Retrieve data for grabbed courses
    courses = []
    if obj_results.count() != 0:
        course_slate = obj_results[0]

        for course in course_slate.classes:
            course_results = Class.objects.filter(shortcode__exact=course)

            if course_results.count() != 0:
                courses.append(course_results[0])

    for course in courses:
        prepare_for_display(course)

    return render(request, 'class_select_result.html', context={'courses': courses})