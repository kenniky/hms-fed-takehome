from django.urls import path
from . import views
import uuid

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('class_select/', views.class_selector, name='class-selector'),
    # For now assign a random learner id
    path('class_submit/', views.class_selector_submit, name='class-selector-submit', kwargs={'learner': uuid.uuid4()}),
    path('class_result/<slug:learner>', views.class_selector_result, name='class-selector-result'),
]