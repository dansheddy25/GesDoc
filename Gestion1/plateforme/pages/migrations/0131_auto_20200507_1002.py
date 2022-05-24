# Generated by Django 3.0.3 on 2020-05-07 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0130_auto_20200507_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Doctorant'),
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
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Doctorant'),
        ),
        migrations.AlterField(
            model_name='individu',
            name='pays',
            field=models.CharField(default='Maroc', max_length=30),
        ),
        migrations.AlterField(
            model_name='msg',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Individu'),
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
        migrations.AlterField(
            model_name='these',
            name='director_these',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Professeur'),
        ),
    ]
