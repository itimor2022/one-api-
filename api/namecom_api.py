# -*- coding: utf-8 -*-
# author: itimor

import sys
import requests

class NamecomApi:
    def __init__(self, key, secret):
        self.url = 'https://api.dev.name.com/v4'
        self.key = key
        self.secret = secret

    def get_domains(self):
        uri = '/domains'
        req = requests.get(self.url + uri, auth=(self.key, self.secret), verify=True)
        print(req.json())
        return req

    def get_domain_info(self, domainName):
        result = self.api.get_domain(domainName)
        domain = result.domain
        print(domain)


if __name__ == '__main__':
    key = "123@gmail.com"
    secret = "123"

    n = NamecomApi(key, secret)
    dt1 = n.get_domains()
    # dt1 = n.get_domain_info('bao0000.com')
    print(dt1)