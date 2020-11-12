# Generated by Django 3.1.2 on 2020-11-07 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0004_participant"),
    ]

    operations = [
        migrations.CreateModel(
            name="FearConditioningData",
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
                ("trial", models.PositiveIntegerField()),
                ("rating", models.PositiveIntegerField()),
                ("conditional_stimulus", models.CharField(max_length=24)),
                ("unconditional_stimulus", models.BooleanField()),
                ("recorded_at", models.DateTimeField()),
                ("volume_level", models.PositiveIntegerField()),
                ("headphones", models.BooleanField()),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="data",
                        to="experiments.fearconditioningmodule",
                    ),
                ),
                (
                    "participant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="experiments.participant",
                    ),
                ),
            ],
        ),
    ]
