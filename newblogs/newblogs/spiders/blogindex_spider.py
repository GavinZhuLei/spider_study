import scrapy
from newblogs.items import IndexItem

class IndexSpider(scrapy.Spider):
    name = 'blogindex'
    allowed_domains = ['cnblogs.com']
    start_urls = [
        'http://www.cnblogs.com',
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        hrefs = sel.xpath('//div[@class="post_item"]/div[@class="post_item_body"]/h3/a/@href').re(r'.+/p/.+')
        items = []
        for href in hrefs:
            item = IndexItem()
            item['href'] = href
            items.append(item)
        return items
