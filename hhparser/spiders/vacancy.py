# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hhparser.items import HhparserItem 

class VacancySpider(CrawlSpider):
    name = 'vacancy'
    allowed_domains = ['hh.ru']
    start_urls = ['https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=0',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=1',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=2']
    rules = (
              Rule(LinkExtractor(allow=('page=2',)), callback='parse'),
             )
    


    def parse(self, response):
        item = HhparserItem()
        item['NameVacancy'] = response.xpath('//div[@class="search-item-name"]//text()').extract()
        item['Salary'] = response.xpath('//div[@class="vacancy-serp-item__compensation"]//text()').extract() 
        item['Employer'] = response.xpath('//div[@class="vacancy-serp-item__meta-info"]//text()').extract()
        yield item
        
        
        