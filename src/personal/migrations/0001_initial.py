# Generated by Django 5.1.2 on 2024-11-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        # migrations.CreateModel(
        #     name="Order",
        #     fields=[
        #         (
        #             "id",
        #             models.BigAutoField(
        #                 auto_created=True,
        #                 primary_key=True,
        #                 serialize=False,
        #                 verbose_name="ID",
        #             ),
        #         ),
        #     ],
        # ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=200, null=True)),
                ("first_name", models.CharField(max_length=200, null=True)),
                ("last_name", models.CharField(max_length=200, null=True)),
                ("major", models.CharField(max_length=200, null=True)),
                ("level", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
