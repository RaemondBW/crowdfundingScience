from scrapy.spider import Spider
from scrapy.selector import Selector

from kickstarter.kicktraqUrls import KicktraqItem

class kickstarterSpider(Spider):
	name = "kicktraq"
	allowed_domains = ["kicktraq.com"]
	start_urls = ["http://www.kicktraq.com/archive/?page=" + str(i) for i in range(1,2000)]

	def parse(self, response):
		
		sel = Selector(response)
		items = []
		for link in sel.xpath('//div[@class="project-infobox"]'):
			item = KicktraqItem()
			item["link"] = "http://www.kicktraq.com" + link.xpath('h2/a/@href').extract()[0]
			items.append(item)

		return items




#getting project price levels sel.xpath('//ul/li/a/h5/span/text()').extract()