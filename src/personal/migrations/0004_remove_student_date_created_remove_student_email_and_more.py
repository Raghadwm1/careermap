# Generated by Django 5.1.2 on 2024-12-04 21:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("personal", "0003_student_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="date_created",
        ),
        migrations.RemoveField(
            model_name="student",
            name="email",
        ),
        migrations.RemoveField(
            model_name="student",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="student",
            name="username",
        ),
    ]
