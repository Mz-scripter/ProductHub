import scrapy
from fake_useragent import UserAgent


class EbaySpider(scrapy.Spider):
    name = "ebay"
    allowed_domains = ["ebay.com"]
    start_urls = ["https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=furniture"]
    
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
        products = response.css("li.s-item")

        for product in products:
            product_link = product.css("a.s-item__link::attr(href)").get()

            if product_link:
                yield response.follow(url=product_link,
                                      callback=self.parse_product_page,
                                      meta={
                                          'category': 'furniture',
                                      }
                                      )
    
    def parse_product_page(self, response):
        name = response.css("#mainContent > div.vim.d-vi-evo-region > div.vim.x-item-title > h1 > span::text").get()
        price = response.css("#mainContent > div.vim.d-vi-evo-region > div.vim.x-price-section.mar-t-20 > div > div > div.x-price-primary > span::text").get()
        image_url = response.css("#PicturePanel > div.vim.x-evo-atf-left-river > div > div > div.x-photos-min-view.filmstrip.filmstrip-x > div.ux-image-carousel-container.image-container > div.ux-image-carousel.zoom.img-transition-medium > div.ux-image-carousel-item.image-treatment.active.image > img::attr(src)").get()
        rating = response.css("span.fdbk-detail-seller-rating__value::text").get()
        review_count = response.css("#s0-1-26-7-18-4-18\[0\]-x-feedback-detail-list-13-tabs-0 > span > span::text").get()
        
        yield {
            'name': name,
            'price': price,
            'image_url': image_url,
            'category': response.meta['category'],
            'rating': rating,
            'review_count': review_count,
        }

