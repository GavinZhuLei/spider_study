# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json


class NewblogsPipeline(object):
    def process_item(self, item, spider):
        return item


class NormalPipeline(object):
    def process_item(self, item, spider):
        if len(item['id']) != 0 and len(item['url']) != 0:
            return item
        else:
             raise DropItem("Missing price in %s" % item)


class SaveDbPipeline(object):
    def __int__(self):
        pass

    def process_item(self, item, spider):
        from newblogs import mysqlstore
        if mysqlstore.is_exist(long(item['id'][0])):
            pass
        else:
            mysqlstore.save_blog(item)
        return item


class SaveLocalPipeline(object):
    def __int__(self):
        pass

    def process_item(self, item, spider):
        filename = item['id'][0] + '.html'
        with open(filename, 'w') as f:
            f.write(item['content'][0].encode('utf-8'))
        return item


class JsonWriterPipeline(object):
    def __int__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item
