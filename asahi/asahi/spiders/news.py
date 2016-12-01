# -*- coding: utf-8 -*-
from ..items import AsahiItem
from scrapy_splash import SplashRequest
import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.tv-asahi.co.jp"]
    start_urls = ['http://news.tv-asahi.co.jp/news_society/articles/000089004.html']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], self.parse,
            args={'wait': 0.5},
        )

    def parse(self, response):
        for res in response.xpath("//div[@id='relatedNews']/div[@class='kanrennews']/ul/li"):
            item = AsahiItem()
            item['related_news'] = res.xpath(".//a/text()").extract()[0].strip()
            yield item
