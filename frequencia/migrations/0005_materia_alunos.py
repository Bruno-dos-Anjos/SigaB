# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0004_auto_20180411_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='alunos',
            field=models.ManyToManyField(to='frequencia.Aluno'),
        ),
    ]