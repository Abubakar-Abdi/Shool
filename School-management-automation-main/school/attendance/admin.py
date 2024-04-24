from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Attendance
# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject','date','present')
    search_fields = ['student', 'subject']
    ordering=['student']
admin.site.register(Attendance, AttendanceAdmin)