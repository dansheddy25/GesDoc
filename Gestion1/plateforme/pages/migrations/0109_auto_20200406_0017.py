# Generated by Django 3.0.3 on 2020-04-05 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0108_auto_20200405_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enregistrement',
            name='articles',
        ),
        migrations.AlterField(
            model_name='candidat',
            name='diplome',
            field=models.ManyToManyField(to='pages.Diplome'),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='individu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.Individu'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='candidat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.Candidat'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Equipe_recherche'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='jury',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Jury'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='these',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.These'),
        ),
        migrations.AlterField(
            model_name='enregistrement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Equipe_recherche'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='individu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.Individu'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='jury',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Jury'),
        ),
    ]