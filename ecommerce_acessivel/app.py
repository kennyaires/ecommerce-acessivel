import settings_dev

from flask import Flask
from scrapy_utils import get_spider_output
from ecommerce_acessivel.spiders.americanas_catalogo import AmericanasCatalogSpider
from ecommerce_acessivel.spiders.americanas_produto import AmericanasProductSpider
from ecommerce_acessivel.serializers import (
    serialize_specifications
)

app = Flask(__name__)
app.config.from_object(settings_dev)


@app.route('/')
def catalogo():
    raw_data = get_spider_output(AmericanasCatalogSpider)
    return f'Catalogo: {raw_data}'


@app.route('/produto/<product_id>')
def produto(product_id):
    raw_data = get_spider_output(AmericanasProductSpider, product_id=product_id)
    print(type(serialize_specifications(raw_data[0]["specifications"])))
    # TODO: throw error if product_id does not exist.
    return f'Produto: {raw_data[0]["name"]}\n Preço: {raw_data[0]["price"]}\n Ficha técnica: {serialize_specifications(raw_data[0]["specifications"])}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)