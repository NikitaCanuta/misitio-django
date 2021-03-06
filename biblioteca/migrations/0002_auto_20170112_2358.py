# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-12 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Editores'},
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
