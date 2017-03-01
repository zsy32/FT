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
                       # unix_socket='/tmp/mysql.sock',
                       user='root',
                       passwd="   ",
                       db='FTTT',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

url='http://www.ftchinese.com/channel/chinareport.html?page=2'

def store(title, content):
    with conn.cursor() as cursor:
        sql = "INSERT INTO `政经` (`title`, `content`) VALUES (%s,%s)"
        cursor.execute(sql, (title, content))
        cursor.connection.commit()
        print("in store")

try:
    for k in range(1, 4):
        new_link = re.sub('page=\d+', 'page=%d' % k, url, re.S)
        response = urllib.request.urlopen(new_link)
        html = response.read()
        page = etree.HTML(html)
        print(k)
        print(new_link)
        title_ = page.xpath('//h2[@class="item-headline"]/a')
        content_ = page.xpath('//div[@class="item-lead"]')
        time = page.xpath('//div[@class="item-time"]')

        j = len(title_)
        for i in range(0, j):
            print(title_[i].text)
            print(content_[i].text)
            print(time[i].text)
            store(title_[i].text,content_[i].text)
            # store('sspk', "dd")

    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `政经` (`title`, `content`) VALUES (%s,%s)"
        cursor.execute(sql, ('', 'very-secret'))
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        conn.commit()

    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT `title`, `content` FROM `政经` WHERE `title`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)

finally:
    conn.close()
# # 创建游标
# cur = conn.cursor()
# # 执行SQL,并返回受影响行数
# cur.execute("USE scraping")
# #random.seed(datetime.datetime.now())
#



#
# cur.execute("SELECT * FROM pages WHERE id=1")
# print(cur.fetchone())
# cur.close()
# conn.close()
# def getLinks(articleUrl):





