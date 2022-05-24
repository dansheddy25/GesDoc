# Generated by Django 3.0.3 on 2020-02-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200228_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diplome',
            name='code_dip',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='type_dip',
            field=models.CharField(choices=[('mst001', 'mst001'), ('mst002', 'mst002'), ('ing001', 'ing001')], default='', max_length=100),
        ),
    ]
