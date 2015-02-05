import scrapy

class CraigslistItem(scrapy.Item):
    """Item object to store name, link, date"""
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()

class CraigslistSpider(scrapy.Spider):
    """
    Tickets spider for NYC
    """
    name = "cl-spider"
    allowed_domains = "craigslist.org"
    start_urls = ['http://newyork.craigslist.org/search/tia#list']

    def parse(self, response):
        sites = response.css('#searchform > div.rightpane > div.content > p')
        items = []
        for site in sites:
            item = CraigslistItem()
            item['title'] = site.css('a::text').extract()
            item['url'] = site.css('a::attr(href)').extract()
            item['date'] = site.css('span.date::text').extract()
            items.append(item)

        return items
