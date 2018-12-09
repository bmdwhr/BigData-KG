import requests
from lxml import etree
import codecs
import csv

s = requests.Session()
for id in range(0, 251):
    url = 'https://movie.douban.com/top250/?start-' + str(id)
    r = s.get(url)
    r.encoding = 'utf-8'
    root = etree.HTML(r.content)
    items = root.xpath('//ol/li/div[@class="item"]')

infolist=[]
for item in items:
    title=item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
    name=title[0].encode('gb2312', 'ignore').decode('gb2312')
        # rank = item.xpath('./div[@class="pic"]/em/text()')[0]
    rating=item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
    print(name, rating)
    infolist.append([name,rating])

with codecs.open('movi.csv', "w", encoding='utf-8-sig')as f:
        writer = csv.writer(f)
        writer.writerow(['序号','影名', '分值'])
        for i,l in enumerate(infolist):   #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
            writer.writerow([i,l[0],l[1]])
