# -*-coding:utf-8-*-
import urllib.request
from lxml import etree
# import re
# url='http://www.hibor.com.cn/doceconomy/index.asp?S_S=%B2%C6%BE%AD&M_M=%B9%FA%C4%DA%B2%C6%BE%AD&flag=0&liflag=0&a=2016-12-31%2021:31:55#location'
# url ='http://www.hibor.com.cn/economy_3.html'
# for k in range(1,4):
#     new_link = re.sub('page=\d+', 'page=%d' % k, url, re.S)
#response = urllib.request.urlopen("http://www.hibor.com.cn/doceconomy/index.asp?S_S=%B2%C6%BE%AD&M_M=%B9%FA%C4%DA%B2%C6%BE%AD&flag=0&liflag=0&a=2017-1-1%2014:01:02#location")
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read()
print (html)
page = etree.HTML(html)
title= page.xpath('/html/body/div/div[3]/div[2]/div[2]')
# title_= page.xpath('//title@*'/a)
    # content = page.xpath('//div[@class="item-lead"]')
    # time = page.xpath('//div[@class="item-time"]')
j=len(title)
for i in range(0,j):
# print(title[0].text)
    print(title[i].text)
        # print(content[i].text)
        # print(time[i].text)http://www.hibor.com.cn/doceconomy/index.asp?S_S=%B2%C6%BE%AD&M_M=%B9%FA%C4%DA%B2%C6%BE%AD&flag=0&liflag=0&a=2016-12-31%2021:31:55#location



