from scrapy.spider import Spider
from scrapy.selector import Selector

from kickstarter.items import KickstarterItem

# how to run:
# scrapy crawl kickstarter -s JOBDIR=crawls -o kickstarter.json -t json

class kickstarterSpider(Spider):
	name = "kickstarter"
	allowed_domains = ["kickstarter.com"]
	#f = open("kickstarterUrls.csv")
	#start_urls = ["https://www.kickstarter.com/projects/papapossum/papa-possums-first-little-book-of-satires/"]
	#start_urls = [url.strip() for url in f.readlines()]
	#f.close()
	

	def parse(self, response):
		item = KickstarterItem()
		sel = Selector(response)
		item['title'] = sel.xpath('//title/text()').extract()[0]
		item['link'] = response.url
		item['description'] = sel.xpath('//div[@class="short_blurb"]/p/text()').extract()[0]
		item['backers'] = sel.xpath('//div[@id="backers_count"]/data/text()').extract()[0]
		#item['totalPledged'] = sel.xpath('//div[@id="pledged"]/data/text()').extract()[0]
		item['goal'] = sel.xpath('//div[@class="num h48 no-margin"]/@data-goal').extract()[0]
		item['totalPledged'] = sel.xpath('//div[@class="num h48 no-margin"]/@data-pledged').extract()[0]
		item['currency'] = sel.xpath('//div[@class="num h48 no-margin"]/data/@data-currency').extract()[0]
		#item['goal'] = sel.xpath('//div[@class="num h48 no-margin"]/data/text()').extract()[1]

		#if len(sel.xpath('//span[@class="money usd no-code"]/text()').extract()) > 0:
		#	item['goal'] = sel.xpath('//span[@class="money usd no-code"]/text()').extract()[0]
		#elif len(sel.xpath('//span[@class="money cad no-code"]/text()').extract()) > 0:
		#	item['goal'] = sel.xpath('//span[@class="money cad no-code"]/text()').extract()[0]
		#else:
		#	item['goal'] = sel.xpath('//span[@class="money gbp no-code"]/text()').extract()[0]
		item['name'] = sel.xpath('//div[@id="creator-name"]/h5/a/text()').extract()[0]
		item['location'] = sel.xpath('//span[@class="location"]/a/text()').extract()[0]
		item['category'] = sel.xpath('//li[@class="category"]/a/text()').extract()[0]
		projectLevels = {}
		levelSelector = sel.xpath('//li[@class="NS-projects-reward"]')
		for level in levelSelector:
			levelInfo = {}
			if len(level.xpath('h5').extract()) > 0:
				amount = level.xpath('h5/span/text()').extract()[0]
				levelInfo["backers"] = int(level.xpath('p/span[@class="backers-wrap"]/span/text()').extract()[0].replace("\n","").split(" ")[0])
				levelInfo["date"] = level.xpath('div[@class="delivery-date"]/time/text()').extract()[0]
				levelInfo["description"] = level.xpath('div[@class="desc"]/p/text()').extract()[0]
				projectLevels[amount] = levelInfo
			else:
				amount = level.xpath('a/h5/span/text()').extract()[0]
				levelInfo["backers"] = int(level.xpath('a/p/span[@class="backers-wrap"]/span/text()').extract()[0].replace("\n","").split(" ")[0])
				levelInfo["date"] = level.xpath('a/div[@class="delivery-date"]/time/text()').extract()[0]
				levelInfo["description"] = level.xpath('a/div[@class="desc"]/p/text()').extract()[0]
				projectLevels[amount] = levelInfo
		item['levels'] = projectLevels

		return item




#getting project price levels sel.xpath('//ul/li/a/h5/span/text()').extract()