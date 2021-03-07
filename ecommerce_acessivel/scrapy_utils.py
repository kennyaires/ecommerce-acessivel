from scrapyscript import Job, Processor
from scrapy.utils.project import get_project_settings


def get_spider_output(spider, **kwargs):
    job = Job(spider, **kwargs)
    processor = Processor(settings=get_project_settings())
    return processor.run([job])
