from scrapy.selector import Selector


def serialize_product_id(value):
    return value.split('/produto/')[1]\
                    .split('?pfm_carac')[0]\
                    .strip()


def serialize_description(value):
    html_items = [Selector(text=p) for p in value]
    description = '\n'.join([_.css('::text').get(default='') for _ in html_items])

    return description


def serialize_specifications(value):
    html_items = [Selector(text=tr) for tr in value]

    specifications = {
        tr.css('td.src__Text-sc-70o4ee-8::text')[0].get().replace('   ', ' '): \
            tr.css('td.src__Text-sc-70o4ee-8::text')[1].get().replace('   ', ' ')\
                for tr in html_items
    }

    return specifications
