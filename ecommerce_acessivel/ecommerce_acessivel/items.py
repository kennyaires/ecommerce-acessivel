# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from ecommerce_acessivel.serializers import (
    serialize_product_id,
    serialize_description,
    serialize_specifications
)


class CatalogAmericanasProduct(scrapy.Item):
    product_id = scrapy.Field(serializer=serialize_product_id)
    url = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    installments = scrapy.Field()


class AmericanasProduct(scrapy.Item):
    product_id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field(serializer=serialize_description)
    specifications = scrapy.Field(serializer=serialize_specifications)
    price = scrapy.Field()
