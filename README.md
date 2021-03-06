# ecommerce-acessivel
Ecommerce Acessivel web app

## Run Scrapy spider

First, go to scrapy project folder.
`cd ecommerce-acessivel`

This will save a json output in the current directory with catalog details:
`scrapy crawl americanas_catalogo -O americanas_catalogo.json`


This will save a json output in the current directory with product details:
`scrapy crawl americanas_produto -O americanas_produto.json -a product_id=2467017682`
