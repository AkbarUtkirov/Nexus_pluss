# Generated by Django 3.2.7 on 2021-10-07 20:56

import ad.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.JSONField(blank=True, default=ad.models.default_location, null=True),
        ),
    ]