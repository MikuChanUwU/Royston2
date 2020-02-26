
import scrapy
class new_spider(scrapy.Spider):
    name = "newSpider"
    start_urls = ["http://172.17.50.43/spicyx"]
    def parse(self, response):
        css_sel = 'img'
        for link in response.css(css_sel):
            new_xsel = '@src'
            yield {'IMAGE Link':link.xpath(new_xsel).extract_first()}
            pg_sel = '.next a ::attr(href)'
            next_page = response.css(pg_sel).extract_first
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)