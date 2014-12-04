__author__ = 'Dop'

from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from craiglist_sample.items import CraiglistSampleItem

class MySpider(CrawlSpider):
    name = "craig"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/"]

    rules = (Rule (LxmlLinkExtractor(allow=("search/no?s=\d00", ),restrict_xpaths=("//span[@class='buttons']",))
             , callback="parse_items", follow = True),
    )


    def parse_items(self,response):
        items = []
        for sel in response.xpath("//span[@class='pl']"):
            item = CraiglistSampleItem()
            item['title'] = sel.xpath("a/text()").extract()
            item['link'] = sel.xpath("a/@href").extract()
            items.append(item)
        yield items


