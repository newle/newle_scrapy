# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class DoubaneventItem(Item):
    # define the fields for your item here like:
    # name = Field()
		event_name = Field()
		event_time = Field()
		event_loc  = Field()
		event_type = Field()
		event_host = Field()
		attent_num = Field()
		willatt_num = Field()
		event_desc = Field()
    #pass
