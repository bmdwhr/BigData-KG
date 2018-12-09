from bs4 import BeautifulSoup
import requests,csv,codecs


url='http://s.dianping.com/yinchuan/group?utm_source=dp_pc_food'
##list-recomend > ul > li:nth-child(1) > div
res=requests.get(url)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'lxml')
"""
获取数据的两种方法select,find
#ht=soup.select('#list-recomend .title')
ht=soup.find('a',{'class':"title"}).get_text()
#bz=soup.select('.group')
#cks=soup.select('.view')
cks=soup.find('span',{'class':"view"}).get_text()
#qls=soup.select('.comment')
qls=soup.find('span',{'class':"comment"}).get_text()
#images=soup.select('#list-recomend .thumb')
images=soup.find('img',{'class':"thumb"})
"""
#使用循环获取所有信息
infolist=[]
for item in soup.find_all('li',{'class':"bghover"}):
    ht=item.find('a',{'class':"title"}).get_text()
    cks=soup.find('span',{'class':"view"}).get_text()
    qls = soup.find('span', {'class': "comment"}).get_text()
    images = soup.find('img', {'class': "thumb"})
    #print(ht, cks, qls, images)
    infolist.append([ht,cks,qls,images])
print(infolist)
#CSV文件
with codecs.open('goods.csv', 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['序号','标题', '查看数', '评论数', '图片'])
    for i,l in enumerate(infolist):
        writer.writerow([i,l[0],l[1],l[2],l[3]])



#print(ht,bz,cks,qls,images,sep='\n**********************\n',end='\n*****')
