# Generated by Django 3.0.3 on 2020-03-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_candidat_cin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidat',
            name='cin',
        ),
    ]
