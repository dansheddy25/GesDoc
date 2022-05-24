# Generated by Django 3.0.3 on 2020-03-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_candidat_cin'),
    ]

    operations = [
        migrations.CreateModel(
            name='nationalite',
            fields=[
                ('code_nat', models.AutoField(primary_key=True, serialize=False)),
                ('libelle_nat', models.CharField(max_length=30)),
                ('cin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.individu')),
            ],
        ),
        migrations.RemoveField(
            model_name='candidat',
            name='cin',
        ),
        migrations.CreateModel(
            name='posseder_nat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.individu')),
                ('code_nat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.nationalite')),
            ],
        ),
    ]