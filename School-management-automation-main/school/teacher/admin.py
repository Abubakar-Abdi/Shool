from django.contrib import admin
from .models import Teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email','subject','gender')
    search_fields = ['first_name', 'last_name', 'email']
    ordering=['first_name']
admin.site.register(Teacher, TeacherAdmin)