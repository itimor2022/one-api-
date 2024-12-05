# -*- coding: utf-8 -*-
# author: itimor

import jwt
from datetime import datetime, timedelta
from django.conf import settings
import time


def gen_token(username):
    key = settings.SECRET_KEY
    payload = {
        'exp': datetime.now() + timedelta(minutes=10),  # 设置过期时间,10分钟
        'iat': datetime.now(),  # 设置发布时间
        'data': {'username': username}  # 添加自定义的数据，为一个包含用户名和昵称的字典
    }
    algorithm = 'HS256'
    token = jwt.encode(payload, key, algorithm)  # 生成byte类型的token
    token = token.decode('utf-8')  # 转为字符串
    return token


def validate_token(token):
    key = settings.SECRET_KEY
    algorithm = 'HS256'
    data = {'results': {}, 'code': '20000', 'msg': '有效的token'}
    try:
        data['results'] = jwt.decode(token, key, algorithm)  # jwt有效、合法性校验
    except jwt.ExpiredSignatureError:
        data['code'] = '40001'
        data['msg'] = 'token已失效'
    except jwt.DecodeError:
        data['code'] = '40002'
        data['msg'] = 'token认证失败'
    except jwt.InvalidTokenError:
        data['code'] = '40003'
        data['msg'] = '非法的token'
    return data


if __name__ == '__main__':
    username = 'aaa'
    token = gen_token(username)
    a = validate_token(token)
    print(a)
