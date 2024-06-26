# Generated by Django 5.0.4 on 2024-04-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "teachers",
                    models.ManyToManyField(
                        related_name="subjects", to="teacher.teacher"
                    ),
                ),
            ],
        ),
    ]
