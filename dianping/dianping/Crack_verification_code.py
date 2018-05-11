import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("../")
from dianping import RClient_dazhong
import json

v2ex_session = requests.Session()

def Crack(url_code,yuan_url):
    header2={
        'Host': 'verify.meituan.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Referer': '''https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=7ad763891b734e2a81fe38f760faf0cb&platform=1&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fwww.dianping.com%252Fshop%252F93710080&theme=dianping''',
        'Content-Length': '1112',
        'Connection': 'keep-alive',
    }


    # url = 'https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=be6708e36cbb463aae339672da33c4e0&platform=1&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fwww.dianping.com%252Fshop%252F22912047&theme=dianping'
    # html = requests.get(url_code,verify=False)
    # print(html.text)
    requestCode = url_code.split('&')[1].replace('requestCode=','')
    # print(requestCode)
    url1 = 'https://verify.meituan.com/v2/captcha?request_code={}&action=spiderindefence&randomId=0.2292928029474346'.format(requestCode)
    html1 = v2ex_session.get(url1,verify=False)
    # print(html1.content)
    rc = RClient_dazhong.RClient('mime123', 'mime@123qwe', '69055', '78248cc50e0c4700843d1f666600c33d')
    # print(rc.rk_create(html1.content, 3040))
    data = 'id=71&request_code={}&captchacode={}'.format(requestCode,rc.rk_create(html1.content, 3040)['Result'])
    html2 = v2ex_session.post('https://verify.meituan.com/v2/ext_api/spiderindefence/verify?id=1&_token=eJxVUWFvmzAQ%2FS%2BWkk9ZwDYEiIQmAslIpXZrl3ZLqmoy2BCrYBNsQrJp%2F32mTbRNPvnePT8%2FnX2%2FwJG1YA7g1J7OwAS0azpUtm3DwJRagTl0kVku9DzozyYg%2F59Dtj8BWfuUgPkzRMifBA5%2BGZgHQzzDANkTaPv2y%2BSKHYORY2JQrY0I7LVu1NyyTCe8OE9rxnVHxDSXtXVEVs8yq2SCtaT60ZCSfSS55lKEquHUXBCUFUzkbNyyQ8eUjiVloevMCmznbuCz3MEQB4TijBbQZX5GqWePm4roQrZ1CMeEkkbLNiSdlmPV5XlMqioj%2BetjW4VvrY1wNEIrE7LRvO7Uh1or%2Fm%2Bbf48Men%2FFA1NdpUd4JVtecmG8RjgZ3EbIHezcwdBsfd9PKSei4aJ8tzKk2svmDTg%2BwjN3hsd6z2oWXoVmMMD8Xr0xv2fy6yWTS9bX%2BtaM0mi5aLphaAOXdVpLcSkUL4WRsJt%2B1T8uv5bn6HZBY69LkyaKV%2FpbGkWbIF1YSZJIHXOsLVwdbr5%2F%2BomKY0%2ByNv98oNkTrKR3wruUrlTpbcn2fonVPmadbSEsArpcnE%2Bnotqdzkt9txbVepESzjb3Xunttun2S8TcPgzB7z8XsMrv',data=data,headers=header2,verify=False)
    # print(html2.text)
    code = (json.loads(html2.text)['data']['response_code'])
    # print(code)
    shop = yuan_url.replace('http://www.dianping.com/shop/','')
    url2 = 'https://optimus-mtsi.meituan.com/optimus/verifyResult?originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2F{}&response_code={}&request_code={}'.format(shop,code,requestCode)
    html3 = v2ex_session.get(url2,verify=False)
    # print(html3.text)
    header3 = {
                'Host': 'www.dianping.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Cookie': '''cy=1; cye=shanghai; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1633d997232c8-06122e8254f41b8-3e6e4647-1fa400-1633d997232c8; _lxsdk=1633d997232c8-06122e8254f41b8-3e6e4647-1fa400-1633d997232c8; _hc.v=e1392e15-aae1-78b0-533a-2b860f10f626.1525746857; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1525746861; Hm_lpvt_4c4fc10949f0d691f3a2cc4ca5065397=1525746861; s_ViewType=10; _lxsdk_s=16349607c13-d6e-aeb-4d4%7C%7C127''',
                'Connection': 'keep-alive',
    }
    html4 = v2ex_session.get(yuan_url ,headers=header3)
    # print(html4.text)
    return html4.text

if __name__ == '__main__':
    url1 = 'https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=1fdf14ea525e4b2c9a19ea8341cc0bb2&platform=1&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fwww.dianping.com%252Fshop%252F93710080&theme=dianping'
    url2 = 'http://www.dianping.com/shop/93710080'
    html = Crack(url1,url2)