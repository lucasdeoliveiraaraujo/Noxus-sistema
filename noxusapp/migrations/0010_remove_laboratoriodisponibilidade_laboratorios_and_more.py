# Generated by Django 5.0.4 on 2024-05-01 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxusapp', '0009_menu_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratoriodisponibilidade',
            name='laboratorios',
        ),
        migrations.AddField(
            model_name='laboratoriodisponibilidade',
            name='laboratorios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='noxusapp.laboratorios'),
        ),
    ]
