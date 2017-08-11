#coding=utf-8
import requests
from bs4 import BeautifulSoup
def content(url):
    text = requests.get(url)
    text.encoding = 'utf-8'
    soup2 = BeautifulSoup(text.text,'html5lib')
    header2 = soup2.select('h1')[0].text
    text2 = soup2.select('#artibody')[0].text
    time2 = soup2.select('.time-source')[0].text
    print(header2,text2,time2,'\n---\n')
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,"html5lib")
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        header = news.select('h2')[0].text
        link = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        # 存入数据库
        print(link,time)
        content(link)