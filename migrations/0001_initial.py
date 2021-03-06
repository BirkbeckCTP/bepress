# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('submission', '0032_auto_20190304_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bepress_id', models.BigIntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.Article')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Journal')),
            ],
        ),
    ]
