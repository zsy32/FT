# -*-coding:utf-8-*-
import urllib.request
from lxml import etree

response = urllib.request.urlopen("http://www.ftchinese.com/story/001070814#adchannelID=1101")
html = response.read()
page = etree.HTML(html)
title = page.xpath('//h1[@class="story-headline"]')
title_ = page.xpath('//h1[@class="story-lead"]/div[@class="story-lead"]')
# time = page.xpath('//h1[@class="story-headline"]'/div[@class="story-byline"])//h1[@class="story-headline"]'
content=page.xpath('//div[@class="story-body"]/p/text()')
print(title[0].text)
# for i in content:
#     print(i)
# print()
#title = page.xpath('//h1[@class="item-headline"]')
#content=page.xpath('//div[@class="item-lead"]')
#time=page.xpath('//div[@class="item-time"]')
#for i in title:
 #for j in content:
 #print(i.text)
   #print (i.text,j.text)

