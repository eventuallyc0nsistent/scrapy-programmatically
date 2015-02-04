import scrapy

class CraigslistItem(scrapy.Item):
    """Item object to store name, link, date"""
    name = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()

class CraigslistSpider(scrapy.Spider):
    """
    Tickets spider for NYC
    """
    name = "cl-spider"
    allowed_domains = "craigslist.org"
    start_urls = ['http://newyork.craigslist.org/tia/']

    def parse(self, response):
        sites = response.css('section.body div#toc_rows div.content p.row span.pl')
        items = []
        for site in sites:
            item = CraigslistItem()
            item['name'] = site.css('a::text').extract()
            item['link'] = site.css('a::attr(href)').extract()
            item['date'] = site.css('span.date::text').extract()
            items.append(item)

        return items
