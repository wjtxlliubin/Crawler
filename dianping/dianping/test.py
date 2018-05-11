import requests

header = {
    'Host': 'www.dianping.com',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Cookie': '''cy=1; cye=shanghai; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1633d997232c8-06122e8254f41b8-3e6e4647-1fa400-1633d997232c8; _lxsdk_s=1633d997232-392-778-d87%7C%7C26; _lxsdk=1633d997232c8-06122e8254f41b8-3e6e4647-1fa400-1633d997232c8; _hc.v=e1392e15-aae1-78b0-533a-2b860f10f626.1525746857; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1525746861; Hm_lpvt_4c4fc10949f0d691f3a2cc4ca5065397=1525746861; s_ViewType=10''',
'Connection': 'keep-alive'
}
html = requests.get('http://www.dianping.com/shop/99250870',headers = header)
print(html.text)