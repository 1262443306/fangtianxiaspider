# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os


class FangtianxiaPipeline:
    i = 1
    detailname ='苏州'
    def __init__(self):
        store_file = os.path.dirname(__file__) + '/spiders/上海周边.csv'
        self.file = open(store_file, 'a+', encoding="utf-8",newline = '')
        # csv写法
        self.writer = csv.writer(self.file, dialect="excel")
    def process_item(self, item, spider):
        name = item['name']
        phone = item['phone']
        mendian = item['mendian']
        print('正在写入.....')
        self.writer.writerow([name,phone,mendian,self.detailname])
        print(name, phone, mendian,'第{}人'.format(self.i))
        print('写入成功!!!!')
        self.i+=1
        return item
    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
