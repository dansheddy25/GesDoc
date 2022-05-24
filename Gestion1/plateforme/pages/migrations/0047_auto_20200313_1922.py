# Generated by Django 3.0.3 on 2020-03-13 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0046_auto_20200313_1921'),
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
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.Individu'),
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
            model_name='posseder_nat',
            name='code_nat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Nationalite'),
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
