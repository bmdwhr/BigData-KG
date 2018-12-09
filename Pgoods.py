import requests
import re      #正则表达式
import csv
import codecs   #自然语言编码转换库


def getHTMLText(url):   #请求url
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()      #抛出异常
        r.encoding = r.apparent_encoding    #r.encoding = ‘xxx’ 模式， 指定编码，apparent_encoding可以获得真实编码
        return r.text
    except:
        return ""


def parsePage(ilt, html):     #页面解析
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)   #正则表达式，以列表的形式返回能匹配的子串,r原始字符
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)

        for i in range(len(plt)):
           price = eval(plt[i].split(':')[1])   #eval()将一个源，当成表达式计算后，赋值给变量
           title = eval(tlt[i].split(':')[1])   #使用冒号分隔键值对，去掉前面的raw_title字段，只获取其中title部分
           ilt.append([price, title])
       # print(ilt)
    except:
        print("")


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    #print(start_url)
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)    #str()将数值转换为字符
            #print(url)
            html = getHTMLText(url)
           # print(html)
            parsePage(infoList, html)
        except:
            continue

    with codecs.open('goods.csv',"w",encoding='utf-8-sig')as f:
        writer=csv.writer(f)
        writer.writerow(['序号','价格','商品名称'])
        for i,l in enumerate(infoList):
            writer.writerow([i,l[0],l[1]])

if __name__ == '__main__':
       main()