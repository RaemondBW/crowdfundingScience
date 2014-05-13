from scrapy.spider import Spider
from scrapy.selector import Selector

from kickstarter.kicktraqUrls import KicktraqItem

class kickstarterURLSpider(Spider):
	name = "kickurl"
	allowed_domains = ["kicktraq.com"]
	#f = open("urls.csv")
	#start_urls = [url.strip() for url in f.readlines()]
	#f.close()

	def parse(self, response):
		
		sel = Selector(response)
		item = KicktraqItem()
		item["link"] = sel.xpath('//div[@id="project-info-image"]/a/@href').extract()[0][:-13]

		return item




#getting project price levels sel.xpath('//ul/li/a/h5/span/text()').extract()