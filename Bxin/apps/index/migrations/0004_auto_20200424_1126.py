# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-24 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200424_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='detail_link',
            field=models.CharField(max_length=80, verbose_name='详情页链接'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_file_id',
            field=models.ImageField(null=True, upload_to='', verbose_name='图片file_id'),
        ),
    ]
