# -*- coding: utf-8 -*-
import os

import scrapy
import time
from items import FangtianxiaItem
class EsfSpider(scrapy.Spider):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    name = 'esf'
    keyword='-a01046-b014445'
    allowed_domains = ['https://sh.esf.fang.com/']
    page = 1
    urls = []
    while page <=100:
        urls.append('https://sh.esf.fang.com/agenthome+'+keyword+'/-i3{}-j310/'.format(page))
        page = page + 1
    start_urls = [url for url in urls]
    def parse(self, response):
        urls = response.xpath('/html/body/div[4]/div[3]/div[2]/ul//@link').extract()
        for i in urls:
            theurl = 'https://sh.esf.fang.com'+i
            req = scrapy.Request(url=theurl,callback=self.parse_detail,dont_filter=True,headers=self.headers)
            yield req
    def parse_detail(self,response):
         items = FangtianxiaItem()
         name= response.xpath('//*[@id="agentname"]/text()').extract_first()
         phone = response.xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/b/text()').extract_first()
         mendian = response.xpath('/html/body/div[3]/div[2]/div[1]/ul[1]/li[3]/span/text()').extract_first()
         items['name']=name
         items['phone'] = phone
         items['mendian']=mendian
         yield items
