# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from newblogs.items import BlogItem

class BlogSpider(CrawlSpider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com']

    rules = (
        Rule(LinkExtractor(allow=('/p/', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)

        sel = scrapy.selector.Selector(response)
        item = BlogItem()
        item['id'] = sel.xpath('//div[@class="post"]/div[@class="postDesc"]/a[last()]/@onclick').re(r'\d+')
        item['time'] = sel.xpath('//div[@class="post"]/div[@class="postDesc"]/span[@id="post-date"]/text()').extract()
        item['title'] = sel.xpath('//div[@class="post"]/h1/a/text()').extract()
        item['url'] = sel.xpath('//div[@class="post"]/h1/a/@href').extract()
        item['content'] = sel.xpath('//div[@class="post"]/div[@class="postBody"]/div[@id="cnblogs_post_body"]').extract()
        return item
