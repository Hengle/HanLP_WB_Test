#! python3
# coding=gbk
import logging
import scrapy

"""
使用 scrapy shell 手动测试网页的响应：
    scrapy shell -s USER_AGENT='Mozilla/5.0' https://movie.douban.com/chart
或者：
    scrapy shell -s USER_AGENT='Mozilla/5.0'
    fetch('https://movie.douban.com/chart')

>>> fetch('https://movie.douban.com/chart')
2020-02-01 20:42:22 [scrapy.core.engine] INFO: Spider opened
2020-02-01 20:42:29 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/robots.txt> (referer: None)
2020-02-01 20:42:35 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/chart> (referer: None)
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # 爬虫的唯一标识
    start_urls_0 = [  # 开始爬取的资源链接列表
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    start_urls = ['https://movie.douban.com/chart']

    # 生成网页链接：可以返回链接的列表，或者写一个链接生成器。
    # def start_requests(self):
    #    urls = [
    #        'http://quotes.toscrape.com/page/1/',
    #        'http://quotes.toscrape.com/page/2/',
    #    ]
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)

    # parse()方法用来解析每个 Request 所下载的响应。它提取爬取的数据作为字典，
    # 还查找要遵循的新 URL 并从中创建新请求（Request）。
    # response 参数是 TextResponse 的一个实例，它保存着下载下来的页面内容。
    def parse(self, response):
        """
        page = response.url.split("/")[-2]
        logging.warning('response.url.split("/") = %s' % response.url.split("/"))
        # [root] WARNING: response.url.split("/") = ['http:', '', 'quotes.toscrape.com', 'page', '1', '']
        filename = 'quotes-wb-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        """
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }


class DoubanSpider(scrapy.Spider):
    name = "douban"

    def start_requests(self):
        url = "https://movie.douban.com/chart"
        yield scrapy.Request(url, callback=self.parse_rank)

    def parse_rank(self, response):
        for item in response.css('tr.item'):
            detail_url = item.css('a.nbg::attr(href)').extract_first()  # 电影的详情链接
            img_url = item.css('a.nbg > img::attr(src)').extract_first()  # 电影的图片链接
            main_name = item.css('div.pl2 > a::text').extract_first()  # 电影的第一个名字
            other_name = item.css('div.pl2 > a > span::text').extract_first(default='/')  # 电影的其它名字，没找到返回一个空格
            brief = item.css('p.pl::text').extract_first()  # 电影简介
            main_name = main_name.replace('\n', '').replace(' ', '')  # 去掉电影名字中的换行符和空格
            other_name = other_name.replace('\n', '').replace(' ', '')

            yield {
                'detail_url': detail_url,
                'img_url': img_url,
                'name': main_name + other_name,
                'brief': brief
            }

            # yield scrapy.Request(url=detail_url + 'comments?status=P',  # 获取短评论页面链接
            #                     callback=self.parse_comments,  # 指定解析函数
            #                     meta={'movie': main_name})  # 传递电影名字

    def parse_comments(self, response):
        for comments in response.css('.comment-item'):
            username = comments.css('span.comment-info > a::text').extract_first()
            comment = comments.css('span.short::text').extract_first()

            yield {
                'movie': response.meta['movie'],
                'username': username,
                'comment': comment
            }

        nexturl = response.css('a.next::attr(href)').extract_first()  # 下一页段评论
        if nexturl:
            yield scrapy.Request(url=response.url[:response.url.find('?')] + nexturl,
                                 callback=self.parse_comments,
                                 meta=response.meta)
