#! python3
# coding=gbk
import logging
import scrapy

"""
ʹ�� scrapy shell �ֶ�������ҳ����Ӧ��
    scrapy shell -s USER_AGENT='Mozilla/5.0' https://movie.douban.com/chart
���ߣ�
    scrapy shell -s USER_AGENT='Mozilla/5.0'
    fetch('https://movie.douban.com/chart')

>>> fetch('https://movie.douban.com/chart')
2020-02-01 20:42:22 [scrapy.core.engine] INFO: Spider opened
2020-02-01 20:42:29 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/robots.txt> (referer: None)
2020-02-01 20:42:35 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://movie.douban.com/chart> (referer: None)
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # �����Ψһ��ʶ
    start_urls_0 = [  # ��ʼ��ȡ����Դ�����б�
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    start_urls = ['https://movie.douban.com/chart']

    # ������ҳ���ӣ����Է������ӵ��б�����дһ��������������
    # def start_requests(self):
    #    urls = [
    #        'http://quotes.toscrape.com/page/1/',
    #        'http://quotes.toscrape.com/page/2/',
    #    ]
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)

    # parse()������������ÿ�� Request �����ص���Ӧ������ȡ��ȡ��������Ϊ�ֵ䣬
    # ������Ҫ��ѭ���� URL �����д���������Request����
    # response ������ TextResponse ��һ��ʵ����������������������ҳ�����ݡ�
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
            detail_url = item.css('a.nbg::attr(href)').extract_first()  # ��Ӱ����������
            img_url = item.css('a.nbg > img::attr(src)').extract_first()  # ��Ӱ��ͼƬ����
            main_name = item.css('div.pl2 > a::text').extract_first()  # ��Ӱ�ĵ�һ������
            other_name = item.css('div.pl2 > a > span::text').extract_first(default='/')  # ��Ӱ���������֣�û�ҵ�����һ���ո�
            brief = item.css('p.pl::text').extract_first()  # ��Ӱ���
            main_name = main_name.replace('\n', '').replace(' ', '')  # ȥ����Ӱ�����еĻ��з��Ϳո�
            other_name = other_name.replace('\n', '').replace(' ', '')

            yield {
                'detail_url': detail_url,
                'img_url': img_url,
                'name': main_name + other_name,
                'brief': brief
            }

            # yield scrapy.Request(url=detail_url + 'comments?status=P',  # ��ȡ������ҳ������
            #                     callback=self.parse_comments,  # ָ����������
            #                     meta={'movie': main_name})  # ���ݵ�Ӱ����

    def parse_comments(self, response):
        for comments in response.css('.comment-item'):
            username = comments.css('span.comment-info > a::text').extract_first()
            comment = comments.css('span.short::text').extract_first()

            yield {
                'movie': response.meta['movie'],
                'username': username,
                'comment': comment
            }

        nexturl = response.css('a.next::attr(href)').extract_first()  # ��һҳ������
        if nexturl:
            yield scrapy.Request(url=response.url[:response.url.find('?')] + nexturl,
                                 callback=self.parse_comments,
                                 meta=response.meta)
