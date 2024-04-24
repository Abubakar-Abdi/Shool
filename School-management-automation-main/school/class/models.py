from django.db import models
from student.models import Student
from teacher.models import Teacher 
from subject.models import Subject
# Create your models here.
class SchoolClass(models.Model):
    class_name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField(Subject)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.class_name

