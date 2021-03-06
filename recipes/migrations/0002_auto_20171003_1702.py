# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instruction',
            name='instruction_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='instruction',
            name='ordinal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
