# Generated by Django 2.0.7 on 2018-07-15 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genetic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='individual_DNA',
            new_name='DNA',
        ),
        migrations.RenameField(
            model_name='optimumdna',
            old_name='DNA_text',
            new_name='DNA',
        ),
    ]
