#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5


class RClient(object):

    def __init__(self, username, password, soft_id, soft_key):
        self.username = username
        self.password = md5(password.encode("utf8")).hexdigest()
        self.soft_id = soft_id
        self.soft_key = soft_key
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    rc = RClient('mime123', 'mime@123qwe', '69055', '78248cc50e0c4700843d1f666600c33d')
    html = requests.get('https://verify.meituan.com/v2/captcha?request_code=eca2a8e638f748d79cc3cab3bedff9d2&action=spiderindefence&randomId=0.24764076676577695',verify=False)
    print()
    print(rc.rk_create(html.content, 3040))