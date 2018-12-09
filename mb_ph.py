from bs4 import BeautifulSoup
import requests
"""
图片反爬取，检查—左上角divers。。——选择手机型号——刷新
Network——Request Headers——User-Agent(复制）
放到headers中
"""

headers={
    'User_Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Mobile Safari/537.36'
}
url='https://www.tripadvisor.cn/Attractions-g293920-Activities-oa30-Phuket.html#FILTERED_LIST'
mb_data=requests.get(url,headers=headers)
soup=BeautifulSoup(mb_data.text,'lxml')
imgs=soup.select('div > img')
for i in imgs:
    print(i.get('src'))
