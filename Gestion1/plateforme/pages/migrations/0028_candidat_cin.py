# Generated by Django 3.0.3 on 2020-03-10 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_remove_candidat_cin'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidat',
            name='cin',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.individu'),
        ),
    ]
