# Generated by Django 3.1.2 on 2020-11-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0010_experiment_rating_delay"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="trial_length",
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
    ]
