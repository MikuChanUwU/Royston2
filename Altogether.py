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
# Use the Request library
import requests
# Set the target webpage
url = 'http://172.17.50.43/spicyx/'
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code
print("Status code")
print("\t OK", r.status_code)
# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t headers.php", x, ":", h.headers[x])
print("**********")
# This will modify the headers user-agent
headers = {'User-Agent' : 'Mobile'}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)