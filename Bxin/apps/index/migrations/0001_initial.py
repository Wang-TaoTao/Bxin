# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-23 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='电影名称')),
                ('score', models.CharField(max_length=10, verbose_name='电影评分')),
                ('desc', models.CharField(max_length=50, null=True, verbose_name='一句话影评')),
                ('image', models.CharField(max_length=80, verbose_name='图片地址')),
                ('detail_link', models.CharField(max_length=80, verbose_name='详情页链接')),
            ],
            options={
                'verbose_name': '电影信息',
                'db_table': 'tb_movie',
            },
        ),
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='电影名称')),
                ('score', models.CharField(max_length=10, verbose_name='电影评分')),
                ('direct', models.CharField(max_length=30, verbose_name='导演')),
                ('etc', models.CharField(max_length=80, verbose_name='编剧')),
                ('performer', models.CharField(max_length=256, verbose_name='主演')),
                ('types', models.CharField(max_length=50, verbose_name='类型')),
                ('address', models.CharField(max_length=50, verbose_name='地区')),
                ('language', models.CharField(max_length=80, verbose_name='语言')),
                ('date', models.CharField(max_length=256, verbose_name='上映日期')),
                ('for_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Movie', verbose_name='index')),
            ],
            options={
                'verbose_name': '电影详情信息',
                'db_table': 'tb_detail',
            },
        ),
    ]
