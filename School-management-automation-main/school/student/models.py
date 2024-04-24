from django.db import models



class Student(models.Model):

    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=False, blank=False)
    age = models.IntegerField(blank=False, null=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gt=0), name='age_gt_zero'),  # Ensures age is greater than zero
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"