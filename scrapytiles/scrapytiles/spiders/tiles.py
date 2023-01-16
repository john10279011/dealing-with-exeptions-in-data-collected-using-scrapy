import scrapy
from ..items import ScrapytilesItem
from scrapy.loader import ItemLoader


class TilesSpider(scrapy.Spider):
    name = "tiles"
    allowed_domains = ["magnatiles.com"]
    start_urls = ["http://magnatiles.com/products/"]

    def parse(self, response):
        for i in response.css("ul.products li"):
            il = ItemLoader(item=ScrapytilesItem(), selector=i)

            il.add_css("name", "h2")
            il.add_css("price", "span.price bdi")
            il.add_css("sku", "a.button::attr(data-product_sku)")

            yield il.load_item()
