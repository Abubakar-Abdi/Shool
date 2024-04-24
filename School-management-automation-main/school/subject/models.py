from django.db import models
from teacher.models import Teacher
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teachers = models.ManyToManyField(Teacher, related_name='subjects')
    def __str__ (self):
        return self.name
    