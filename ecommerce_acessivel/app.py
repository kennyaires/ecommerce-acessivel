import settings_dev

from flask import Flask, render_template
from scrapy_utils import get_spider_output
from ecommerce_acessivel.spiders.americanas_catalogo import AmericanasCatalogSpider
from ecommerce_acessivel.spiders.americanas_produto import AmericanasProductSpider
from ecommerce_acessivel.serializers import (
    serialize_specifications,
    serialize_product_id,
    serialize_description,
    serialize_specifications
)

app = Flask(__name__)
app.config.from_object(settings_dev)


@app.route('/')
def catalogo():
    products = get_spider_output(AmericanasCatalogSpider)
    for p in products:
        p['product_id'] = serialize_product_id(p['product_id'])

    
    return render_template('catalogo.html', products=products)


@app.route('/produto/<product_id>')
def produto(product_id):
    
    try:
        product = get_spider_output(AmericanasProductSpider, product_id=product_id)[0]
        product['description'] = serialize_description(product['description'])
        product['specifications'] = serialize_specifications(product['specifications'])
        return render_template('produto.html', product=product)
    except:
        return render_template('erro.html')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0')