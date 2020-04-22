# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64


import logging
import base64


logger = logging.getLogger(__name__)
# 隧道服务器
tunnel_master_host  = "tps158.kdlapi.com"
tunnel_master_port  = 15818
# 备用隧道host和端口
tunnel_slave_host = "tps131.kdlapi.com"
tunnel_slave_port = 15818
# 切换阀值
threshold = 3
# 隧道id和密码
tid = "t18756237644575"
password = "wangtaotao"



# 代理中间件
class ProxyDownloadMiddleware(object):

    def process_request(self, request, spider):
        global threshold
        if threshold > 0:
            host, port = tunnel_master_host, tunnel_master_port
        else:
            host, port = tunnel_slave_host, tunnel_slave_port
        if request.url.startswith("http://"):
            proxy_url = 'http://{host}:{port}'.format(host=host, port=port)
        elif request.url.startswith("https://"):
            proxy_url = 'https://{host}:{port}'.format(host=host, port=port)
        request.meta['proxy'] = proxy_url  # 设置代理
        logger.debug("using proxy: {}".format(request.meta['proxy']))
        # 隧道代理需要进行身份验证
        #
        # 用户名和密码需要先进行base64编码，然后再赋值
        username_password = "{tid}:{password}".format(tid=tid, password=password)
        b64_username_password = base64.b64encode(username_password.encode('utf-8'))
        request.headers['Proxy-Authorization'] = 'Basic ' + b64_username_password.decode('utf-8')
        threshold -= 1
        return None


class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
