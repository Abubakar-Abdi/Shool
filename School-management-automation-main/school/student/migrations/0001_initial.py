# Generated by Django 5.0.4 on 2024-04-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("student_id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("MALE", "Male"), ("FEMALE", "Female")], max_length=10
                    ),
                ),
                ("age", models.IntegerField()),
            ],
        ),
        migrations.AddConstraint(
            model_name="student",
            constraint=models.CheckConstraint(
                check=models.Q(("age__gt", 0)), name="age_gt_zero"
            ),
        ),
    ]
