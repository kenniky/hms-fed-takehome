from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('class_select/', views.class_selector, name='class-selector'),
    path('class_submit/', views.class_selector_submit, name='class-selector-submit'),
]