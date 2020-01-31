#! python3
# coding=gbk
import logging
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # 爬虫的唯一标识
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # 生成网页链接：可以返回链接的列表，或者写一个链接生成器。
    # def start_requests(self):
    #    urls = [
    #        'http://quotes.toscrape.com/page/1/',
    #        'http://quotes.toscrape.com/page/2/',
    #    ]
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)

    # parse()方法用来解析相应，它处理为每个请求下载的响应。它提取爬取的数据作为字典，
    # 还查找要遵循的新 URL 并从中创建新请求（Request）。
    # response 参数是 TextResponse 的一个实例，它保存着页面内容。
    def parse(self, response):
        page = response.url.split("/")[-2]
        logging.warning('response.url.split("/") = %s' % response.url.split("/"))
        # [root] WARNING: response.url.split("/") = ['http:', '', 'quotes.toscrape.com', 'page', '1', '']
        filename = 'quotes-wb-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # self.log('Saved file %s' % filename)
