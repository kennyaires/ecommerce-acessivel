import scrapy

from ecommerce_acessivel.items import CatalogAmericanasProduct


class AmericanasCatalogSpider(scrapy.Spider):
    name = "americanas_catalogo"

    start_urls = ['https://www.americanas.com.br/categoria/moveis/sala-de-jantar']

    def parse(self, response):
        for item in response.css('div.product-grid-item'):
            yield self.parse_catalog(item)

    def parse_catalog(self, item):
        def extract_with_css(query):
            return item.css(query).get(default='').strip()

        fields = {
            'product_id': extract_with_css('div.RippleContainer-sc-1rpenp9-0>a::attr(href)'),
            'url': extract_with_css('div.RippleContainer-sc-1rpenp9-0>a::attr(href)'),
            'description': extract_with_css('h2.TitleUI-bwhjk3-15::text'),
            'rating': extract_with_css('div.SvgFilledWrapper-sc-1fg2071-2>svg>desc::text'),
            'price': item.css('span.PriceUI-bwhjk3-11::text')[1].get(),
            'installments': extract_with_css('span.Installment-bwhjk3-7::text')
        }

        return CatalogAmericanasProduct(**fields)
