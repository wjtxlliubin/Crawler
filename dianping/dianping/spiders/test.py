# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
#import daizhong_test_ma
import json

header3 = {
'Host': 'www.dianping.com',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Cookie': '''cy=1; cye=shanghai; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1633d997232c8-06122e8254f41b8-3e6e4647-1fa400-1633d997232c8; _lxsdk=1633d997232c8-06122e8254f41b8-3e6e4647-1fa400-1633d997232c8; _hc.v=e1392e15-aae1-78b0-533a-2b860f10f626.1525746857; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1525746861; Hm_lpvt_4c4fc10949f0d691f3a2cc4ca5065397=1525746861; s_ViewType=10; _lxsdk_s=1634d0bdfcf-f66-bcf-f92%7C%7C63''',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
}
html4 = requests.get('http://www.dianping.com/shop/76839896',headers=header3)
print(html4.text)
soup = BeautifulSoup(html4.text, 'lxml')
shop_name = soup.find('div',class_="shop-name").find('h1').get_text()
rank_level = soup.find('div',class_="rank").find('span').get('class')
rank = soup.find('div',class_="rank").find_all('span',class_="item")
phone = soup.find('div',class_="phone").find_all('span',class_="item J-phone-hide")
address = soup.find('div',class_="address").get_text().replace('地址：','').replace(' ','').replace('\n','')
for i in rank:
    if '效果' in i.get_text():
        print(i.get_text().replace('效果：',''))
    if '师资' in i.get_text():
        print(i.get_text().replace('师资：',''))
    if '环境' in i.get_text():
        print(i.get_text().replace('环境：', ''))
print(str(int(rank_level[1].replace('mid-str',''))/10)+'星')
print(shop_name)
for i in phone:
    print(i.get('data-phone'))
print(address)
class_shop = soup.find_all('div',class_="item notag")
for i in class_shop:
    print(i.find('p',class_="title").get_text())
    print(i.find('div',class_="price").find('span',class_="cur").get_text().replace('\n','').replace(' ',''))
shop_info = soup.find('div',id="info").find('ul',class_="con").find_all('li')
for i in shop_info:
    if i.find("span",class_="title").get_text() == "商户介绍":
        print(i.get_text())
    if i.find("span",class_="title").get_text() == "特色服务":
        print(i.get_text())
