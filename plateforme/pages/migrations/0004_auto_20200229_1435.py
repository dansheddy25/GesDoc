# Generated by Django 3.0.3 on 2020-02-29 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200228_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diplome',
            name='libelle_dip',
        ),
        migrations.AddField(
            model_name='individu',
            name='code_dip',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pages.diplome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diplome',
            name='code_dip',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
