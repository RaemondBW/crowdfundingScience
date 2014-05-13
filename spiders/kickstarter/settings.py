# Scrapy settings for kickstarter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kickstarter'

SPIDER_MODULES = ['kickstarter.spiders']
NEWSPIDER_MODULE = 'kickstarter.spiders'
DOWNLOAD_DELAY = .5
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kickstarter (+http://www.yourdomain.com)'
