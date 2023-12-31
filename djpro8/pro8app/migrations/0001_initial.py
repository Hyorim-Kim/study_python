# Generated by Django 5.0a1 on 2023-10-20 04:19
# 물리적인 테이블이 만들어짐

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (  # 장고가 자동으로 AutoField를 만들어줌, 얘가 primary key이며 자동증가함
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("pub_date", models.DateTimeField()),
            ],
        ),
    ]
