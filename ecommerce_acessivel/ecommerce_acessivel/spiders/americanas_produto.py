import scrapy

from ecommerce_acessivel.items import AmericanasProduct


class AmericanasProductSpider(scrapy.Spider):
    name = "americanas_produto"

    def __init__(self, product_id, **kwargs):
        self.start_urls = [f'https://www.americanas.com.br/produto/{product_id}']
        self.product_id = product_id
        super().__init__(**kwargs)

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        fields = {
            'product_id': self.product_id,
            'name': extract_with_css('span.src__Text-sc-154pg0p-0::text'),
            'description': [_.get() for _ in response.css('div.src__Description-sc-13f3i2j-3>p')],
            'specifications': [_.get() for _ in response.css('table.src__SpecsCell-sc-70o4ee-6>tbody>tr')],
            'price': response.css('div.src__BestPrice-sc-1jvw02c-5::text')[1].get()
        }
        
        return AmericanasProduct(**fields)
