#!/usr/bin/python
# -*- coding:utf8 -*-

import hmac
import hashlib
import urllib3
import time
import requests
from base64 import b64encode
from collections import OrderedDict
import json
from urllib.parse import urlencode, unquote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def init_header(user, token):
    header = {}
    key = '{}:{}'.format(user, token)
    b64string = b64encode(bytes(key, "utf-8"))
    header['AUTHORIZATION'] = 'Basic %s' % bytes.decode(b64string)
    return header


def make_signature(secret_key, data):
    hashed = hmac.new(bytes(secret_key.encode("utf-8")), bytes(data.encode("utf-8")), hashlib.sha1)
    return hashed.hexdigest()


def make_sorted_param_string(param):
    ''' 将参数排序并序列化为字符串
    '''
    param = OrderedDict(sorted(param.items()))
    data = urlencode(param)
    return unquote(data)


class VsApi(object):
    def __init__(self):
        self.api_prefix = 'https://www.vishnuplus.com/api/v3'
        self.api_id = '111'
        self.api_key = '222'
        self.__header = dict()

    def http_request(self, method, uri, params):
        """
        接收请求，返回结果
        """
        t = int(time.time())
        params.update(time=t)
        url = self.api_prefix + uri
        data = make_sorted_param_string(params)
        signature = make_signature(self.api_key, data)
        headers = init_header(self.api_id, signature)

        if method == 'GET':
            req = requests.get(url, params=params, verify=False, headers=headers)
        elif method == 'POST':
            req = requests.post(url, json=params, verify=False, headers=headers)
        elif method == 'PUT':
            req = requests.put(url, json=params, verify=False, headers=headers)
        elif method == 'DELETE':
            req = requests.delete(url, json=params, verify=False, headers=headers)
        else:
            return {'msg': 'router method not match!'}

        return req.json()

    def get_site(self):
        uri = '/site'
        method = 'GET'
        data = {
            'page': 120
        }
        req = self.http_request(method, uri, data)
        return req

    def get_sites(self):
        uri = '/site'
        method = 'GET'
        data_list = []
        for i in range(1, 200):
            print('page %s' % i)
            data = {
                'page': i
            }
            req = self.http_request(method, uri, data)
            if req['data']['total'] == 0:
                break
            for item in req['data']['sites']:
                data_list.append({
                    'site_id': item['id'],
                    'domain': item['domain'],
                    'status': True,
                })
        return data_list

    def purge_cache(self, site_id, type, domain, url):
        uri = '/site/purge'
        method = 'POST'
        if type == 'host':
            urls = [domain]
        else:
            urls = [domain + url]
        data = {
            'sid': site_id,
            'type': type,
            'urls': json.dumps(urls)
        }
        req = self.http_request(method, uri, data)
        return req


if __name__ == '__main__':
    # site api
    api = VsApi()
    # 同步站点
    print(api.get_site())
    # print(api.get_sites())
    # 清除缓存
    site_id = '123'
    a = api.purge_cache(site_id, 'host', 'http://123.com', '')
    print(a)
