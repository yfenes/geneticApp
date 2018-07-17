# Generated by Django 2.0.7 on 2018-07-15 23:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genetic', '0002_auto_20180716_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='precision',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]