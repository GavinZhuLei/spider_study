# -*- coding: utf-8 -*-

# Scrapy settings for newblogs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newblogs'

SPIDER_MODULES = ['newblogs.spiders']
NEWSPIDER_MODULE = 'newblogs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newblogs (+http://www.yourdomain.com)'


ITEM_PIPELINES = {
    'newblogs.pipelines.NormalPipeline': 1,
    'newblogs.pipelines.SaveDbPipeline': 2,
    # 'newblogs.pipelines.SaveLocalPipeline':3,
    # 'newblogs.pipelines.JsonWriterPipeline': 800,
}
