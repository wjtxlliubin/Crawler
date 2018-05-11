# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import hashlib
from dianping import Crack_verification_code
from urllib import parse
from dianping.items import DianpingItem
from bs4 import BeautifulSoup

class DazhongdianpingSpider(scrapy.Spider):
    name = 'dazhongdianping'
    allowed_domains = ['www.dianping.com']
    # start_urls = ['http://www.dianping.com/']
    start_url = "http://www.dianping.com/shanghai/ch75/g2872"
    cookies = {
        'navCtgScroll':0 ,
        '_lxsdk_cuid':'16251bee35cc8-0eb126b2ee11028-1269624a-1fa400-16251bee35cc8',
        '_lxsdk':'16251bee35cc8-0eb126b2ee11028-1269624a-1fa400-16251bee35cc8',
        '_hc.v':'d18adecd-eb83-5151-6f9f-364124670865.1521789887',
        's_ViewType':'10',
        'cy':'1',
        'cye':'shanghai',
        '_lx_utm':'utm_source%3DBaidu%26utm_medium%3Dorganic',
        'Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397':'1524707265',
        'Hm_lpvt_4c4fc10949f0d691f3a2cc4ca5065397':'1524731503',
        '_lxsdk_s':'1630102546c-dc1-723-fef%7C%7C68',
    }
    def start_requests(self):
        yield scrapy.Request(url=self.start_url,cookies=self.cookies,callback=self.parse,dont_filter=True, method='get')# 这里带着cookie发出请求

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        body = soup.find('div', class_="nc-contain").find('div',class_="con").find('div',class_="nc-items").find_all('a')
        total_href = []
        for i in body:
            total_dict = {}
            print(i.get('href'))
            print(i.find('span').get_text())
            total_dict['url'] = i.get('href')
            total_dict['name_ser'] = i.find('span').get_text()
            total_href.append(total_dict)
        print(total_href)
        for item in total_href:
            item['url']
            yield scrapy.Request(url=item['url'],cookies=self.cookies,callback=self.parse_detail,dont_filter=True,meta={'url':item['url'],'name_ser':item['name_ser']})# 这里带着cookie发出请求

    def parse_detail(self, response):
        name_ser = response.meta['name_ser']
        soup = BeautifulSoup(response.body, 'lxml')
        body = soup.find('div',id="shop-all-list").find_all('li')
        for i in body:
            detail_url = i.find('div',class_="txt").find('div',class_="tit").find('a').get("href")
            yield scrapy.Request(url=detail_url,cookies=self.cookies,callback=self.parse_detail_de,dont_filter=True,meta={'url':detail_url,'name_ser':name_ser})# 这里带着cookie发出请求
            

        next_page= soup.find('div',class_="page").find('a',class_="next")
        if next_page:
            next_page_url = next_page.get("href")
            yield scrapy.Request(url=next_page_url,cookies=self.cookies,callback=self.parse_detail,dont_filter=True,meta={'url':response.url,'name_ser':item['name_ser']})# 这里带着cookie发出请求

    def parse_detail_de(self, response):
        name_ser = response.meta['name_ser']
        url = response.meta['url']
        print('++++++++++++++++++')
        print(url)
        print(response.url)
        # print(response.body)
        if 'https://verify.meituan.com/v2/web/general_page?' in response.url:
            html = Crack_verification_code.Crack(response.url,url)
        else:
            html = response.body
            # print(response.url.split('&')[1].replace('requestCode=',''))
            # print(html)
        item = DianpingItem()
        soup = BeautifulSoup(str(html),'lxml')
        shop_name = soup.find('div',class_="shop-name").find('h1').get_text()
        rank_level = soup.find('div',class_="rank").find('span').get('class')
        rank = soup.find('div',class_="rank").find_all('span',class_="item")
        phone = soup.find('div',class_="phone").find_all('span',class_="item J-phone-hide")
        address = soup.find('div',class_="address").get_text().replace('地址：','').replace(' ','').replace('\n','')
        for i in rank:
            if '效果' in i.get_text():
                item['effection'] = i.get_text().replace('效果：','')
            if '师资' in i.get_text():
                item['teachers'] = i.get_text().replace('师资：','')
            if '环境' in i.get_text():
                item['environment'] = i.get_text().replace('环境：', '')
        item['star'] = str(int(rank_level[1].replace('mid-str',''))/10)+'星'
        item['name'] = shop_name
        phone_list = []
        for i in phone:
            phone_list.append(i.get('data-phone'))
        item['address'] = address
        item['phone'] = phone_list
        class_shop = soup.find_all('div',class_="item notag")
        class_list = []
        for i in class_shop:
            class_dict = {}
            class_dict['class_name'] = i.find('p',class_="title").get_text()
            class_dict['class_price'] = i.find('div',class_="price").find('span',class_="cur").get_text().replace('\n','').replace(' ','')
        shop_info = soup.find('div',id="info").find('ul',class_="con").find_all('li')
        for i in shop_info:
            if i.find("span",class_="title").get_text() == "商户介绍":
                item['description'] = i.get_text().replace('\r\n','').replace(' ','').replace('\n','')
            if i.find("span",class_="title").get_text() == "特色服务":
                character = i.get_text().replace(' ','').split('\n')
                item['characteristic'] = [ i for i in character if i !=''][1:]
        item['_id'] = self.hash_distanct(item['name'],item['address'])
        yield item


    def hash_distanct(self,name,adress):
        '''
        md5去重
        :param : app_name
        :return:
        '''
        md5 = hashlib.md5()
        md5.update(name.encode('utf-8')+adress.encode('utf-8'))
        return md5.hexdigest() 