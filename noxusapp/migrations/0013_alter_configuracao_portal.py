# Generated by Django 5.0.4 on 2024-05-06 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxusapp', '0012_configuracao_portal_configuracao_senha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracao',
            name='portal',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
