# Generated by Django 3.0.3 on 2020-03-04 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20200305_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidat',
            name='cin',
        ),
    ]
