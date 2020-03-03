# Generated by Django 2.2.10 on 2020-03-03 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0078_auto_20200221_0257"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=64)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("url", models.URLField(max_length=256)),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order.Order",
                    ),
                ),
            ],
        ),
    ]
