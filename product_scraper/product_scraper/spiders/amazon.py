import scrapy
from fake_useragent import UserAgent


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=electronics"]

    def start_requests(self):
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        }

        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        products = response.css("div.s-result-item[data-component-type=s-search-result]")

        for product in products:
            yield {
                'name': product.css("h2>a>span::text").get(),
                'price': product.css(".a-price[data-a-size=xl] .a-offscreen::text").get(),
                'image_url': product.css("img.s-image::attr(src)").get(),
                'rating': product.css("span[aria-label~=stars]::attr(aria-label)").get(),
                'review_count': product.css("span[aria-label~=stars] + span::attr(aria-label)").get(),
                'source': 'amazon',
                'category': 'electronics'
            }