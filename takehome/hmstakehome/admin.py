from django.contrib import admin

# Register your models here.
from .models import Class, ClassSlate

admin.site.register(Class)
admin.site.register(ClassSlate)