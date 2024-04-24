from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subject
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'teachers']
   
    ordering=['name']
admin.site.register(Subject, SubjectAdmin)