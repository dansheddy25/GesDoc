# Generated by Django 3.0.3 on 2020-03-15 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0053_auto_20200315_1442'),
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
            model_name='diplome',
            name='type_dip',
            field=models.CharField(choices=[('mst001', 'mst001'), ('mst002', 'mst002'), ('ing001', 'ing001')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='id_these',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.These'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='ref_compte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Compte'),
        ),
        migrations.AlterField(
            model_name='equipe_recherche',
            name='code_prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Professeur'),
        ),
        migrations.AlterField(
            model_name='equipe_recherche',
            name='id_doctorant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Doctorant'),
        ),
        migrations.AlterField(
            model_name='individu',
            name='etat_civil',
            field=models.CharField(choices=[('Celibataire', 'Celibataire'), ('Marié', 'Marié'), ('Veuf/Veuve', 'Veuf/Veuve')], max_length=15),
        ),
        migrations.AlterField(
            model_name='individu',
            name='genre',
            field=models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=15),
        ),
        migrations.AlterField(
            model_name='jury',
            name='code_prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Professeur'),
        ),
        migrations.AlterField(
            model_name='labo',
            name='id_equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Equipe_recherche'),
        ),
        migrations.AlterField(
            model_name='posseder_dip',
            name='code_dip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Diplome'),
        ),
        migrations.AlterField(
            model_name='posseder_dip',
            name='id_doctorant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Doctorant'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='id_doctorant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Doctorant'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='ref_compte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Compte'),
        ),
    ]
