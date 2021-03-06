# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManagement', '0004_auto_20160729_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultytimetable',
            name='period1',
        ),
        migrations.AddField(
            model_name='facultytimetable',
            name='period1',
            field=models.ManyToManyField(related_name='period1', to='StudentManagement.Period'),
        ),
        migrations.RemoveField(
            model_name='facultytimetable',
            name='period2',
        ),
        migrations.AddField(
            model_name='facultytimetable',
            name='period2',
            field=models.ManyToManyField(blank=True, null=True, related_name='period2', to='StudentManagement.Period'),
        ),
        migrations.RemoveField(
            model_name='facultytimetable',
            name='period3',
        ),
        migrations.AddField(
            model_name='facultytimetable',
            name='period3',
            field=models.ManyToManyField(blank=True, null=True, related_name='period3', to='StudentManagement.Period'),
        ),
        migrations.RemoveField(
            model_name='facultytimetable',
            name='period4',
        ),
        migrations.AddField(
            model_name='facultytimetable',
            name='period4',
            field=models.ManyToManyField(blank=True, null=True, related_name='period4', to='StudentManagement.Period'),
        ),
        migrations.RemoveField(
            model_name='facultytimetable',
            name='period5',
        ),
        migrations.AddField(
            model_name='facultytimetable',
            name='period5',
            field=models.ManyToManyField(blank=True, null=True, related_name='period5', to='StudentManagement.Period'),
        ),
        migrations.RemoveField(
            model_name='period',
            name='section',
        ),
        migrations.AddField(
            model_name='period',
            name='section',
            field=models.ManyToManyField(to='StudentManagement.Class'),
        ),
        migrations.RemoveField(
            model_name='period',
            name='subject',
        ),
        migrations.AddField(
            model_name='period',
            name='subject',
            field=models.ManyToManyField(to='StudentManagement.Subject'),
        ),
        migrations.RemoveField(
            model_name='subjectattendencetable',
            name='subject',
        ),
        migrations.AddField(
            model_name='subjectattendencetable',
            name='subject',
            field=models.ManyToManyField(to='StudentManagement.Subject'),
        ),
    ]
