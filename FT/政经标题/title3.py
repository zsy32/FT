# -*-coding:utf-8-*-
import urllib.request
from lxml import etree
import re
import datetime
import random
import pymysql.cursors

aaa = "123"
# 创建链接(connect to the database)
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd="   ",
                       db='FT2',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

url = 'http://www.ftchinese.com/channel/chinareport.html?page=2'
# list_=[chinareport, chinabusiness, chinamarkets, chinastock, chinaproperty, culture, chinaopinion]

def store(title, content, time):
    with conn.cursor() as cursor:
        sql = "INSERT INTO `政经` (title, content, time) VALUES (%s,%s,%s)"
        # sql = "UPDATE `政经` SET title=%s, content=%s, time=%s"
        cursor.execute(sql, (title, content, time))
        cursor.connection.commit()
        print("in store")

try:
    with conn.cursor() as cursor:
        sql = "DELETE FROM  `政经` "
        cursor.execute(sql)
        cursor.connection.commit()

    for k in range(1, 4):
        new_link = re.sub('page=\d+', 'page=%d' % k, url, re.S)
        response = urllib.request.urlopen(new_link)
        html = response.read()
        page = etree.HTML(html)
        print("政经")
        print(k)
        print(new_link)
        title_ = page.xpath('//h2[@class="item-headline"]/a')
        content_ = page.xpath('//div[@class="item-lead"]')
        time = page.xpath('//div[@class="item-time"]')

        j = len(title_)
        for i in range(0, j):
            print(title_[i].text)
            print(content_[i].text)
            print(time[i].text, type(time[i].text))
            store(title_[i].text, content_[i].text, time[i].text)
            # store('sspk', "dd",'uuu')

finally:
    conn.close()







