from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from doubanevent.items import DoubaneventItem

class doubanEvent_Spider(CrawlSpider):

	name = "douban_event"
	allowed_domains = ['douban.com']
	start_urls = ['http://beijing.douban.com/']
	rules = [Rule(SgmlLinkExtractor(allow=['http://www\.douban\.com/event/\d+/']), 'parseevent')]

	def parseevent(self, response):
		sel = Selector(response)
		event = DoubaneventItem()
		event['event_name'] = sel.xpath("//h1/text()").extract()
		event_time = sel.xpath("//li[@class=calendar-str-item]").extract()
#		event_loc  = Field()
#		event_type = Field()
#		event_host = Field()
#		attent_num = Field()
#		willatt_num = Field()
#		event_desc = Field()
		return event
