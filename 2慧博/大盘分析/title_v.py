# -*-coding:utf-8-*-
import urllib.request
from lxml import etree
import re
url='http://www.hibor.com.cn/doceconomy/index.asp?S_S=%B2%C6%BE%AD&M_M=%B9%FA%C4%DA%B2%C6%BE%AD&flag=0&liflag=0&a=2016-12-31%2021:31:55#location'
# for k in range(1,4):
#     new_link = re.sub('page=\d+', 'page=%d' % k, url, re.S)
response = urllib.request.urlopen(url)
html = response.read()
page = etree.HTML(html)

    title = page.xpath('//title')
    # content = page.xpath('//div[@class="item-lead"]')
    # time = page.xpath('//div[@class="item-time"]')
    j = len(title)
    for i in range(0, j):
        print(title[i].text)
        # print(content[i].text)
        # print(time[i].text)http://www.hibor.com.cn/doceconomy/index.asp?S_S=%B2%C6%BE%AD&M_M=%B9%FA%C4%DA%B2%C6%BE%AD&flag=0&liflag=0&a=2016-12-31%2021:31:55#location



