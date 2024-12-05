# -*- coding: utf-8 -*-
# author: itimor

import requests
import time


class XXLJOB:

    def __init__(self, xxljob_info):
        self.api_url = xxljob_info["api_url"]
        self.username = xxljob_info["username"]
        self.password = xxljob_info["password"]
        # 定义请求header
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        # 获取cookies
        self.cookies = self.login()

    def request(self, uri, payload=None, method="POST"):
        url = self.api_url + uri
        if method == "POST":
            req = requests.post(url=url, data=payload, headers=self.headers, cookies=self.cookies)
        else:
            req = requests.get(url=url, cookies=self.cookies)
        return req.json()

    def login(self):
        uri = '/login'
        payload = {
            "userName": self.username,
            "password": self.password,
            "ifRemember": "on"
        }
        req = requests.post(self.api_url + uri, data=payload, headers=self.headers)
        return req.cookies

    def add(self, payload):
        uri = '/jobinfo/add'
        req = self.request(uri, payload)
        return req

    def update(self, payload):
        uri = '/jobinfo/update'
        req = self.request(uri, payload)
        return req

    def remove(self, payload):
        uri = '/jobinfo/remove'
        req = self.request(uri, payload)
        return req

    def start(self, payload):
        uri = '/jobinfo/start'
        req = self.request(uri, payload)
        return req

    def stop(self, payload):
        uri = '/jobinfo/stop'
        req = self.request(uri, payload)
        return req

    def save(self, payload):
        uri = '/jobcode/save'
        req = self.request(uri, payload)
        return req

    def chatinfo(self, payload):
        uri = '/chartInfo'
        req = self.request(uri, payload)
        return req

    def jobgroup(self, payload=None):
        uri = '/jobgroup/'
        req = self.request(uri, payload, method="GET")
        return req


if __name__ == '__main__':
    xxljob_info = {
        "api_url": "xxx",
        "username": "xxx",
        "password": "xxx",
    }
    jobapi = XXLJOB(xxljob_info)

    # add job
    # payload = {
    #     'jobGroup': 1,
    #     'jobDesc': 'test123',
    #     'executorRouteStrategy': 'FIRST',
    #     'jobCron': '0 */1 * * * ?',
    #     'glueType': 'GLUE_PYTHON',
    #     'executorHandler': None,
    #     'executorBlockStrategy': 'SERIAL_EXECUTION',
    #     'childJobId': None,
    #     'executorTimeout': 0,
    #     'executorFailRetryCount': 0,
    #     'author': 'xman',
    #     'alarmEmail': None,
    #     'executorParam': "bw app",
    # }
    # jobapi.add(payload)
    # payload = {
    #     'id': 55
    # }
    # jobapi.remove(payload)
    # payload["jobDesc"] = "testxxx"
    # jobapi.update(payload)
    # payload = {
    #     'id': 10,
    #     'glueSource': '456',
    #     'glueRemark': 'update{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # }
    # data = jobapi.save(payload)
    # from datetime import datetime, timedelta
    #
    # endDate = datetime.now()
    # startDate = endDate -  timedelta(days=7)
    # payload = {
    #     'startDate': startDate.strftime("%Y-%m-%d") + " 00:00:00",
    #     'endDate': endDate.strftime("%Y-%m-%d") + " 23:59:59"
    # }
    data = jobapi.jobgroup()
    print(data)


