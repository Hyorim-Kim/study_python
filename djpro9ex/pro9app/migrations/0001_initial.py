# Generated by Django 5.0a1 on 2023-10-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("irum", models.CharField(max_length=10)),
                ("juso", models.CharField(max_length=20)),
                ("nai", models.IntegerField()),
            ],
        ),
    ]
