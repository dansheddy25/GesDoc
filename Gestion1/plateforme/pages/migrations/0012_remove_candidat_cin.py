# Generated by Django 3.0.3 on 2020-03-04 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidat',
            name='cin',
        ),
    ]
