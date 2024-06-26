# Generated by Django 5.0.4 on 2024-05-06 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxusapp', '0011_configuracao_alter_laboratorios_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracao',
            name='portal',
            field=models.IntegerField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='configuracao',
            name='senha',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='configuracao',
            name='tls',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
