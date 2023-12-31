# Generated by Django 5.0a1 on 2023-10-23 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Maker",
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
                ("mname", models.CharField(max_length=20)),
                ("mtel", models.CharField(max_length=30)),
                ("maddr", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("pname", models.CharField(max_length=20)),
                ("pprice", models.IntegerField()),
                (
                    "pmaker_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pro12app.maker"
                    ),
                ),
            ],
        ),
    ]
