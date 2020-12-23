# Generated by Django 3.1.2 on 2020-11-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0005_fear_conditioning_data"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="basemodule",
            options={"ordering": ["sortorder"]},
        ),
        migrations.AlterField(
            model_name="participant",
            name="participant_id",
            field=models.CharField(max_length=24, unique=True),
        ),
    ]
