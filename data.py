import requests,csv
from bs4 import BeautifulSoup
import codecs   #自然语言编码转换库

def main():
    res=requests.get("http://book.dangdang.com/20180504_by11")
    res.encoding = res.apparent_encoding  #获得真实编码
    soup=BeautifulSoup (res.text,'lxml')
    info=[]
    for item in soup.select('#bd li'):
        names=item.select('.name')[0].text.strip()
        price_n=item.select('.price span')[2].text.strip()
        price_f = item.select('.price span')[3].text.strip()
        price=price_n+price_f
        info.append([names,price])
    print(info)

    with codecs.open('book.csv','w',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '书名', '价格'])
        for i,l in enumerate(info):
            writer.writerow([i,l[0],l[1]])



    #print(price,text,image,sep='\n**********************\n',end='\n*****')#多变量值分隔


if __name__ == '__main__':
    main()


