# Generated by Django 3.0.3 on 2020-03-02 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200301_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individu',
            name='password',
        ),
        migrations.RemoveField(
            model_name='individu',
            name='username',
        ),
    ]
