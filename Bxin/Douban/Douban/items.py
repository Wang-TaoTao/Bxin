# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import scrapy

from scrapy_djangoitem import DjangoItem
from apps.index import models

#
class DoubanItem(DjangoItem):
    django_model = models.Movie

# class DoubanItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field()
#     # info = scrapy.Field()
#     score = scrapy.Field()
#     desc = scrapy.Field()
#     image = scrapy.Field()
#     detail_link = scrapy.Field()


class DoubanDetailItem(DjangoItem):

    django_model = models.MovieDetail

# class DoubanDetailItem(scrapy.Item):
#
#     direct = scrapy.Field()
#     etc = scrapy.Field()
#     performer = scrapy.Field()
#     types=scrapy.Field()
#     address = scrapy.Field()
#     language=scrapy.Field()
#     date =scrapy.Field()



