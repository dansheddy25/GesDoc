# Generated by Django 3.0.3 on 2020-03-12 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0033_remove_nationalite_cin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorant',
            name='num_insc',
        ),
        migrations.RemoveField(
            model_name='individu',
            name='est_admin',
        ),
        migrations.RemoveField(
            model_name='individu',
            name='password',
        ),
        migrations.RemoveField(
            model_name='individu',
            name='username',
        ),
        migrations.RemoveField(
            model_name='posseder_nat',
            name='cin',
        ),
    ]
