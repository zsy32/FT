# -*-coding:utf-8-*-
import urllib.request
from lxml import etree
import re
import datetime
import random
import pymysql.cursors
# 创建链接(connect to the database)
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd="   ",
                       db='FT2',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

url1 = 'http://www.ftchinese.com/channel/'
url2 = '.html?page=1'
# list_ = ['chinareport', 'chinabusiness', 'chinamarkets', 'chinastock', 'chinaproperty', 'culture', 'chinaopinion']
list_table = ["政经", "商业", "金融市场"]
list_url = ['chinareport', 'chinabusiness', 'chinamarkets']
# EMPLOYEE = ["政经", "商业", "金融市场"]
list_table_len = len(list_table)
list_url_len = len(list_url)


def store(tableName, title, content, time):
    with conn.cursor() as cursor:
        #     sql = "INSERT INTO `list_[0]` (title, content, time) VALUES (%s,%s,%s)"
        # # sql = "UPDATE `政经` SET title=%s, content=%s, time=%s"
        # elif print("商业"):
        #     sql = "INSERT INTO `list_[1]` (title, content, time) VALUES (%s,%s,%s)"
        # else :
        sql = "INSERT INTO "+tableName+" (title, content, time) VALUES (%s,%s,%s)"
        cursor.execute(sql, (title, content, time))
        cursor.connection.commit()

try:
    with conn.cursor() as cursor:
        # 如果数据表已经存在使用 execute() 方法删除表。

        for table in range(0, list_table_len):
            sql = 'DROP TABLE IF EXISTS ' + list_table[table]
            print(sql)
            cursor.execute(sql)
        # 创建数据表SQL语句
            sql = 'CREATE TABLE '+list_table[table]+'''(
                     id INT(11),
                     title  VARCHAR(400)  NULL,
                     content  VARCHAR(10000) NULL,
                     time  VARCHAR(100) NULL,
                     sign VARCHAR(50) NULL,
                     score  VARCHAR(50) NULL )'''
            cursor.execute(sql)
            cursor.connection.commit()

    for urls in range(0, list_url_len):
        url = url1 + list_url[urls] + url2
        print(list_table[urls])
        for k in range(1, 4):
            new_link = re.sub('page=\d+', 'page=%d' % k, url, re.S)
            response = urllib.request.urlopen(new_link)
            html = response.read()
            page = etree.HTML(html)
            print(k)
            print(new_link)
            tableName = list_table[urls]
            title_ = page.xpath('//h2[@class="item-headline"]/a')
            content_ = page.xpath('//div[@class="item-lead"]')
            time_ = page.xpath('//div[@class="item-time"]')
            j = len(title_)
            for m in range(0, j):
                print(title_[m].text)
                print(content_[m].text)
                print(time_[m].text)
                print("存入"+tableName+"中")
                store(tableName, title_[m].text, content_[m].text, time_[m].text)
#
finally:
    conn.close()







