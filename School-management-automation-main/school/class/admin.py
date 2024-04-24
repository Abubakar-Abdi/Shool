

# Register your models here.
from django.contrib import admin
from .models import SchoolClass, Subject, Teacher, Student

class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'class_teacher')
    filter_horizontal = ('subjects', 'students')
admin.site.register(SchoolClass,SchoolClassAdmin)