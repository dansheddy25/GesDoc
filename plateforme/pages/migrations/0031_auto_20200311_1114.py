# Generated by Django 3.0.3 on 2020-03-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individu',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='individu_pics'),
        ),
    ]
