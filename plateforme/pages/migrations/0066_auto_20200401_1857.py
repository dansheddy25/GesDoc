# Generated by Django 3.0.3 on 2020-04-01 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0065_auto_20200401_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidat',
            old_name='num_insc',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='candidat',
            old_name='accept',
            new_name='preSelection',
        ),
        migrations.RenameField(
            model_name='diplome',
            old_name='code_dip',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='doctorant',
            old_name='id_doctorant',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='equipe_recherche',
            old_name='id_equipe',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='professeur',
            old_name='code_prof',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='these',
            old_name='id_these',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='candidat',
            name='date',
        ),
        migrations.RemoveField(
            model_name='doctorant',
            name='date_dip',
        ),
        migrations.RemoveField(
            model_name='equipe_recherche',
            name='id_doctorant',
        ),
        migrations.RemoveField(
            model_name='professeur',
            name='id_doctorant',
        ),
        migrations.RemoveField(
            model_name='professeur',
            name='ref_compte',
        ),
        migrations.AddField(
            model_name='candidat',
            name='selection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='candidat',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.Candidat'),
        ),
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
            name='ref_compte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Compte'),
        ),
        migrations.DeleteModel(
            name='posseder_dip',
        ),
    ]
