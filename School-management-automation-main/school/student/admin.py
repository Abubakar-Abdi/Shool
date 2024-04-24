


# Register your models here.
from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name'),
    search_fields = ['first_name']
    ordering=['first_name']
admin.site.register(Student, StudentAdmin)