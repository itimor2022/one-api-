# -*- coding: utf-8 -*-
# author: itimor

from requests_toolbelt import MultipartEncoder
import requests

domain_file = "domain.txt"

# websiteId
websiteId_list = [
    {"SiteName": "live.yangguangxueyuan01.shop", "websiteId": "43"},
    {"SiteName": "live.yangguangxueyuan02.shop", "websiteId": "44"},
    {"SiteName": "live.yangguangxueyuan03.shop", "websiteId": "45"},
    {"SiteName": "live.yangguangxueyuan04.shop", "websiteId": "46"},
    {"SiteName": "live.yangguangxueyuan05.shop", "websiteId": "47"},
    {"SiteName": "live.yangguangxueyuan06.shop", "websiteId": "48"},
    {"SiteName": "live.yangguangxueyuan07.shop", "websiteId": "49"},
    {"SiteName": "live.yangguangxueyuan08.shop", "websiteId": "50"},
    {"SiteName": "live.yangguangxueyuan09.shop", "websiteId": "51"},
    {"SiteName": "live.yangguangxueyuan10.shop", "websiteId": "52"},
]

url = "http://api.9hdam.cfd:55520/api/getShortLink?DomainId=28"

with open(domain_file, 'w') as fn:
    n = 10
    for room in range(1001, 1011):
        print(f"{room}房间:")
        fn.write(f"{room}房间:")
        fn.write("\n")
        if room > 1004:
            n = 5
        for k, i in enumerate(websiteId_list):
            if k > n:
                continue
            data = MultipartEncoder(
                fields={
                    "oldLink": f":55520/?room={room}",
                    "SiteName": i["SiteName"],
                    "short_id": "5",
                    "websiteId": i["websiteId"],
                    "pc": "1",
                    "wechat": "2"
                }
            )
            headers = {
                'Content-Type': data.content_type
            }
            r = requests.post(url, data=data, headers=headers)
            f_data = f'{r.text}'
            print(f_data)
            fn.write(f_data)
            fn.write("\n")

print(f"域名文件已生成，请打开{domain_file}查看")
