from django.forms import ModelForm
from .models import Student 



class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'gender', 'age')