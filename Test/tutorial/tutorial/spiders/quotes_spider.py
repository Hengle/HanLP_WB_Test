#! python3
# coding=gbk
import logging
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # �����Ψһ��ʶ
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    # ������ҳ���ӣ����Է������ӵ��б�����дһ��������������
    # def start_requests(self):
    #    urls = [
    #        'http://quotes.toscrape.com/page/1/',
    #        'http://quotes.toscrape.com/page/2/',
    #    ]
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)

    # parse()��������������Ӧ��������Ϊÿ���������ص���Ӧ������ȡ��ȡ��������Ϊ�ֵ䣬
    # ������Ҫ��ѭ���� URL �����д���������Request����
    # response ������ TextResponse ��һ��ʵ������������ҳ�����ݡ�
    def parse(self, response):
        page = response.url.split("/")[-2]
        logging.warning('response.url.split("/") = %s' % response.url.split("/"))
        # [root] WARNING: response.url.split("/") = ['http:', '', 'quotes.toscrape.com', 'page', '1', '']
        filename = 'quotes-wb-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # self.log('Saved file %s' % filename)
