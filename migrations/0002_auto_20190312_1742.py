# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0032_auto_20190304_0916'),
        ('bepress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedarticle',
            name='started',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='importedarticle',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='submission.Article'),
        ),
        migrations.AlterUniqueTogether(
            name='importedarticle',
            unique_together=set([('article', 'bepress_id')]),
        ),
    ]
