# -*- coding: utf-8 -*-
import scrapy

class SpidernameSpider(scrapy.Spider):
    name = 'spidername'
    page_number = 2
    allowed_domains = ['www.farfetch.com']
    start_urls = ['https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx/']


    def parse(self, response):
        for product in response.xpath("//*[@id='slice-container']/div[3]/div/div[2]/div/div[1]/ul/li"):
            brand = product.xpath(".//a/div[2]/h3[@class='_346238']/text()").get()
            name = product.xpath(".//a/div[2]/p/text()").get()
            price = product.xpath(".//a/div[2]/div/span/text()").get()
            purl = product.xpath(".//a/@href").get()
            isrc = product.xpath(".//a/meta/@content").get()

            yield {
                'product_name': name,
                'brand_name': brand,
                'product_price': price,
                'product_url': purl,
                'product_img': isrc
            }


        next_page = response.xpath("//*[@id='slice-container']/div[3]/div/div[2]/div/div[2]/div/div[3]/a/@href")
        if next_page:
            next_page = response.urljoin(next_page.get())
            yield response.follow(url=next_page, callback=self.parse)












