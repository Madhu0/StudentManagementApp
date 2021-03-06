# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManagement', '0005_auto_20160729_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultytimetable',
            name='period2',
            field=models.ManyToManyField(null=True, related_name='period2', to='StudentManagement.Period'),
        ),
        migrations.AlterField(
            model_name='facultytimetable',
            name='period3',
            field=models.ManyToManyField(null=True, related_name='period3', to='StudentManagement.Period'),
        ),
        migrations.AlterField(
            model_name='facultytimetable',
            name='period4',
            field=models.ManyToManyField(null=True, related_name='period4', to='StudentManagement.Period'),
        ),
        migrations.AlterField(
            model_name='facultytimetable',
            name='period5',
            field=models.ManyToManyField(null=True, related_name='period5', to='StudentManagement.Period'),
        ),
        migrations.RemoveField(
            model_name='period',
            name='subject',
        ),
        migrations.AddField(
            model_name='period',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StudentManagement.Subject'),
        ),
    ]
