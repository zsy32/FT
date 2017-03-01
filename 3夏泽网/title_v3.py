# -*-coding:utf-8-*-
import urllib.request
from lxml import etree
import re

url = 'http://nianjian.xiaze.com/info/'
response = urllib.request.urlopen(url)
html = response.read()
page = etree.HTML(html)
title_ = page.xpath('//ul[@class="e2"]/li/b/a')
title = page.xpath('//ul[@class="e2"]/li/a[2]')
date_ = page.xpath('//ul[@class="e2"]/li/span/small[1]')
date = page.xpath('//ul[@class="e2"]/li/span/text()[2]')
content = page.xpath('//ul[@class="e2"]//li/p')
j = len(title_)
for i in range(0, j):
    print(title_[i].text)
    if title[i].text is None:
        k = i + 1
        title__ = page.xpath('//ul[@class="e2"]/li[%d]/a[2]/b' % k)
        print(title__[0].text)
    else:
        print(title[i].text)
    print(date_[i].text, date[i])
    # print(date[i])
    print(content[i].text)









