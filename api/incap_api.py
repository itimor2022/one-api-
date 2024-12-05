#!/usr/bin/python
# -*- coding:utf8 -*-

import requests

account_list = [222]


class IncapApi(object):
    def __init__(self):
        self.data = {
            'api_id': '111',
            'api_key': '222',
        }
        self.api_prefix = 'https://my.incapsula.com/api/prov/v1'

    def get_accounts(self):
        """
        暂不可用
        """
        uri = '/accounts/list'
        url = self.api_prefix + uri
        req = requests.post(url, data=self.data)
        return req.json()

    def get_sites(self):
        uri = '/sites/list'
        url = self.api_prefix + uri
        data_list = []
        for i in account_list:
            print(i)
            self.data.update(
                page_size=100,
                account_id=i
            )
            req = requests.post(url, data=self.data).json()
            for item in req['sites']:
                if len(item['dns']) > 0:
                    data_list.append({
                        'account_id': item['account_id'],
                        'site_id': item['site_id'],
                        'domain': item['domain'],
                        'cname': item['dns'][0]['set_data_to'][0],
                    })
                else:
                    data_list.append({
                        'account_id': item['account_id'],
                        'site_id': item['site_id'],
                        'domain': item['domain'],
                        'cname': '',
                    })
        return data_list

    def purge_cache(self, site_id, purge_pattern=''):
        uri = '/sites/cache/purge'
        url = self.api_prefix + uri
        self.data.update(
            site_id=site_id,
            purge_pattern=purge_pattern
        )
        req = requests.post(url, data=self.data).json()
        return req


if __name__ == '__main__':
    # site api
    api = IncapApi()
    # 同步站点
    # print(api.get_sites())
    # 清除缓存
    site_id = '88951568'
    a = api.purge_cache(site_id=site_id, purge_pattern='eqweqfqio##@!00')
    print(a)
