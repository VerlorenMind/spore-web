# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-07 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(max_length=40)),
                ('snr', models.DecimalField(decimal_places=3, max_digits=5)),
                ('schedule', models.IntegerField()),
                ('n', models.IntegerField()),
                ('k', models.IntegerField()),
                ('r', models.DecimalField(decimal_places=3, max_digits=5)),
                ('stddev', models.FloatField()),
                ('fer', models.FloatField()),
            ],
        ),
    ]
