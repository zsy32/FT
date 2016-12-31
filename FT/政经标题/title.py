# -*-coding:utf-8-*-
import urllib.request
from lxml import etree
import re
url='http://www.ftchinese.com/channel/chinareport.html?page=2'
for k in range(1,4):
      new_link = re.sub('page=\d+', 'page=%d' % k, url, re.S)
      response =urllib.request.urlopen(new_link)
      html = response.read()
      page = etree.HTML(html)
      print(k)
      print(new_link)
      title = page.xpath('//h2[@class="item-headline"]/a')
      content = page.xpath('//div[@class="item-lead"]')
      time = page.xpath('//div[@class="item-time"]')
      j = len(title)
      for i in range(0, j):
        print(title[i].text)
        print(content[i].text)
        print(time[i].text)



