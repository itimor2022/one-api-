# -*- coding: utf-8 -*-
# author: itimor

import requests
import json

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class FalconClient(object):
    def __init__(self, endpoint=None, user=None, password=None, keys=[], session=None, ssl_verify=True):
        self._endpoint = endpoint
        self._url_prex = '/api/portal/'
        self._keys = keys
        self._session = session
        self.ssl_verify = ssl_verify

        if not session:
            params = {
                "name": user,
                "password": password
            }
            self._session = requests.Session()
            ret = self.do_request('get', 'self/profile', params=params)
            api_token = {
                "name": user,
                "sig": ret.get("sig")
            }
            self._session.auth = (user, password)
            self._session.headers.update({
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json',
                'Apitoken': json.dumps(api_token)
            })

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]

        return self.__class__(
            endpoint=self._endpoint,
            keys=self._keys + [key],
            session=self._session,
            ssl_verify=self.ssl_verify)

    def __getitem__(self, key):
        """Look up an option value and perform string substitution."""
        return self.__getattr__(key)

    def __call__(self, **kwargs):
        method = self._keys[-1]
        url = "/".join(self._keys[0:-1])
        url = url.replace("_", "-")
        return self.do_request(method, url, **kwargs)

    def do_request(self, method, url, params=None, data=None):
        url = self._endpoint + self._url_prex + url
        print(url)
        if data:
            print(data)

        if params is None:
            params = {}

        if method == 'get' or method == 'list':
            response = self._session.get(url, params=params, verify=self.ssl_verify)

        if method == 'post' or method == 'create':
            response = self._session.post(url, params=params, json=data, verify=self.ssl_verify)

        if method == 'put' or method == 'update':
            response = self._session.put(url, json=data, verify=self.ssl_verify)

        if method == 'delete':
            response = self._session.delete(url, params=params, json=data, verify=self.ssl_verify)

        try:
            body = json.loads(response.text)
        except ValueError:
            body = "Get unknow error is [%s]" % response.reason

        return body


if __name__ == '__main__':
    cli = FalconClient(endpoint="http://n9e.xxoo.com", user='root', password='root')
    # 列出10个用户
    # params = {"limit": 10}
    # r = cli.user.list(params=params)
    # 创建用户
    # params = {
    #     "username": "aaa",
    #     "password": "123456",
    #     "dispname": "艾斯",
    #     "phone": "18888888888",
    #     "email": "aaa@qq.com",
    #     "im": "518",
    # }
    # r = cli.user.create(data=params)
    # 查看已收录的监控对象
    # params = {"limit": 10, "field": "ident"}
    # r = cli.endpoint.list(params=params)
    # 根据标识查找监控对象
    params = {"batch": "192.168.0.111"}
    r = cli.endpoint.get(params=params)
    # 节点列表
    # params = {"limit": 10}
    # r = cli.tree.list(params=params)
    # 查看某个节点的对象
    # params = {"limit": 10, "field": "ident"}
    # r = cli.node['1'].endpoint.list(params=params)
    # 修改监控对象别名
    # params = {"alias": "bj-bb-01"}
    # r = cli.endpoint['2'].update(data=params)
    # 节点下挂载监控对象
    # params = {"idents": ["192.168.0.112"], "del_old": 0}
    # r = cli.node['2'].endpoint_bind.post(data=params)
    # 节点下解挂监控对象
    # params = {"idents": ["192.168.0.112"]}
    # r = cli.node['2'].endpoint_unbind.post(data=params)
    print(r)
