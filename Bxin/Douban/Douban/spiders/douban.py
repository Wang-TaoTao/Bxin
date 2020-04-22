# -*- coding: utf-8 -*-
import scrapy
import time

from Bxin.settings import logger
from Douban.items import DoubanItem

from Douban.items import DoubanDetailItem


class MovieSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        el_list = response.xpath('//*[@class="info"]')

        for el in el_list:
            temp = DoubanItem()

            try:
                temp['name'] = el.xpath('./div[1]/a/span[1]/text()').extract_first()
            except Exception as e:
                logger.error(e)
                print("{}111获取失败name".format(temp['name']))
            # info = el.xpath('./*[@class="bd"]/p[1]/text()').extract_first()
            # item['info'] = info.split('\n')[1].strip()
            try:
                temp['score'] = el.xpath('./div[2]/div/span[2]/text()').extract_first()
            except Exception as e:
                logger.error(e)
                print("{}111获取失败score".format(temp['name']))

            try:
                temp['desc'] = el.xpath('./div[2]/p[2]/span/text()').extract_first()
            except Exception as e:
                logger.error(e)
                print("{}111获取失败desc".format(temp['name']))
            # 图片地址
            try:
                temp['image'] = el.xpath('../div/a/img/@src').extract()[0]
            except Exception as e:
                logger.error(e)
                print("{}111获取失败image".format(temp['name']))
            # 详情页链接
            try:
                temp['detail_link'] = el.xpath('../div[2]/div/a/@href').extract()[0]
            except Exception as e:
                logger.error(e)
                print("{}111获取失败desc".format(temp['name']))

            if temp['detail_link']:

                yield scrapy.Request(url=temp['detail_link'],
                                     callback=self.movie_detail,
                                     meta={"mv":temp},
                                     )
                time.sleep(5)



            yield temp



        # 翻页
        url = response.xpath("//span[@class='next']/a/@href").extract_first()
        if url != None:
            url = response.urljoin(url)
            yield scrapy.Request(
                url = url,
                # priority=1,
            )



    def movie_detail(self, response):

        '''处理每个电影的详情页面'''
        item = response.meta['mv']
        temp = DoubanDetailItem()


        detail_all = response.xpath('//*[@id="info"]').extract()
        detail_all = str(detail_all)

        import re
        from w3lib.html import remove_tags

        detail_all_thr = eval(remove_tags(detail_all))

        # 电影名
        try:
            temp['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        except Exception as e:
            print("{}获取失败name".format(temp['name']))
        # 分数
        try:
            temp['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        except Exception as e:
            print("{}获取失败score".format(temp['name']))
        # 导演
        try:
            direct = detail_all_thr[0].split('\n')[1]
            temp['direct'] = "".join(direct).split(":")[1].strip()
        except Exception as e:
            logger.error(e)
            print("{}获取失败direct".format(temp['name']))
        # 编剧
        try:
            etc = detail_all_thr[0].split('\n')[2].split('/')[:2]
            temp['etc'] = "".join(etc).strip().split(":")[1].strip()
        except Exception as e:

            temp['etc'] = "null"
            logger.error(e)
            print("{}获取失败etc".format(temp['name']))
        # 主演 只取前5个人
        try:
            performer = detail_all_thr[0].split('\n')[3].split('/')[:5]
            temp['performer'] = "".join(performer).strip().split(":")[1].split("类型")[0]
        except Exception as e:
            logger.error(e)
            print("{}获取失败performer".format(temp['name']))

        # 类型
        try:
            types = detail_all_thr[0].split('\n')[4]
            temp['types'] = "".join(types).strip().split(":")[1].strip()
        except Exception as e:
            logger.error(e)
            print("{}获取失败types".format(temp['name']))
        # 地区
        try:
            address = detail_all_thr[0].split('\n')[6]
            temp['address'] = "".join(address).strip().split(":")[1].strip()
        except Exception as e:
            logger.error(e)
            print("{}获取失败address".format(temp['name']))
        # 语言
        try:
            language = detail_all_thr[0].split('\n')[7]
            temp['language'] = "".join(language).strip().split(":")[1].strip()
        except Exception as e:
            logger.error(e)
            print("{}获取失败language".format(temp['name']))
        # 日期
        try:
            date = detail_all_thr[0].split('\n')[8]
            temp['date'] = "".join(date).strip().split(":")[1].strip()
        except Exception as e:
            logger.error(e)
            print("{}获取失败date".format(temp['name']))

        yield temp






