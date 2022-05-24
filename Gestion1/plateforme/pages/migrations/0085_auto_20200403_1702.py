# Generated by Django 3.0.3 on 2020-04-03 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0084_auto_20200403_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admini',
            name='code_jury',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Jury'),
        ),
        migrations.AlterField(
            model_name='admini',
            name='ref_compte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Compte'),
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
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='pages.Equipe_recherche'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='these',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.These'),
        ),
        migrations.AlterField(
            model_name='equipe_recherche',
            name='professeur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.Professeur'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='professeur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.Professeur'),
        ),
        migrations.AlterField(
            model_name='labo',
            name='id_equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Equipe_recherche'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='individu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.Individu'),
        ),
    ]
