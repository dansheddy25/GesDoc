# Generated by Django 3.0.3 on 2020-03-04 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_candidat_cin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='cin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.individu'),
        ),
    ]
