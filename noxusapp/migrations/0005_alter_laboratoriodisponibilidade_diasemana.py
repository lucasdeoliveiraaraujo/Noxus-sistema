# Generated by Django 5.0.4 on 2024-04-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxusapp', '0004_laboratoriodisponibilidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoriodisponibilidade',
            name='diaSemana',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]
