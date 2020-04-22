# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-22 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200422_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetail',
            name='address',
            field=models.CharField(max_length=30, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='date',
            field=models.CharField(max_length=30, verbose_name='上映日期'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='direct',
            field=models.CharField(max_length=30, verbose_name='导演'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='etc',
            field=models.CharField(max_length=30, verbose_name='编剧'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='language',
            field=models.CharField(max_length=30, verbose_name='语言'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='performer',
            field=models.CharField(max_length=80, verbose_name='主演'),
        ),
        migrations.AlterField(
            model_name='moviedetail',
            name='types',
            field=models.CharField(max_length=30, verbose_name='类型'),
        ),
    ]
