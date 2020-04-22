# -*- coding: utf-8 -*-
import scrapy
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
            temp['name'] = el.xpath('./div[1]/a/span[1]/text()').extract_first()
            # info = el.xpath('./*[@class="bd"]/p[1]/text()').extract_first()
            # item['info'] = info.split('\n')[1].strip()
            temp['score'] = el.xpath('./div[2]/div/span[2]/text()').extract_first()
            temp['desc'] = el.xpath('./div[2]/p[2]/span/text()').extract_first()
            # 图片地址
            temp['image'] = el.xpath('../div/a/img/@src').extract()[0]

            # 详情页链接
            temp['detail_link'] = el.xpath('../div[2]/div/a/@href').extract()[0]

            if temp['detail_link']:
                yield scrapy.Request(url=temp['detail_link'],
                                     callback=self.movie_detail,
                                     meta={"mv":temp},
                                     )
            yield temp


        # 翻页
        url = response.xpath("//span[@class='next']/a/@href").extract_first()
        if url != None:
            url = response.urljoin(url)
            yield scrapy.Request(
                url = url,
            )



    def movie_detail(self, response):

        '''处理每个电影的详情页面'''
        item = response.meta['mv']
        temp = DoubanDetailItem()

        detail_all= response.xpath('//*[@id="info"]').extract()
        detail_all=str(detail_all)

        import re
        from w3lib.html import remove_tags

        detail_all_thr = eval(remove_tags(detail_all))


        # 导演
        direct = detail_all_thr[0].split('\n')[1]
        temp['direct'] = "".join(direct).split(":")[1].strip()
        # 编剧
        etc = detail_all_thr[0].split('\n')[2]
        temp['etc'] = "".join(etc).strip().split(":")[1].strip()
        # 主演 只取前5个人
        performer = detail_all_thr[0].split('\n')[3].split('/')[:5]
        temp['performer'] = "".join(performer).strip().split(":")[1].split("类型")[0]
        # 类型
        types = detail_all_thr[0].split('\n')[4]
        temp['types'] = "".join(types).strip().split(":")[1].strip()
        # 地区
        address = detail_all_thr[0].split('\n')[6]
        temp['address'] = "".join(address).strip().split(":")[1].strip()
        # 语言
        language = detail_all_thr[0].split('\n')[7]
        temp['language'] = "".join(language).strip().split(":")[1].strip()
        # 日期
        date = detail_all_thr[0].split('\n')[8]
        temp['date'] = "".join(date).strip().split(":")[1].strip()

        yield temp





