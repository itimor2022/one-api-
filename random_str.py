# -*- coding: utf-8 -*-
# author: itimor

import random
import string

src_digits = string.digits  # string_数字  '0123456789'
src_uppercase = string.ascii_uppercase  # string_大写字母 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
src_lowercase = string.ascii_lowercase  # string_小写字母 'abcdefghijklmnopqrstuvwxyz'
src_special = string.punctuation  # strin_特殊字符 '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def gen_random_char(chars):
    # shuffle将一个序列中的元素随机打乱，打乱字符串
    random.shuffle(chars)
    str = ''.join(chars)
    return str


def gen_user(length):
    # sample从序列中选择n个随机独立的元素，返回列表
    num = random.sample(src_digits, 1)  # 随机取1位数字
    lower = random.sample(src_uppercase, 1)  # 随机取1位小写字母
    other = random.sample(src_digits + src_lowercase, length)  # 随机取4位
    chars = num + lower + other
    str = gen_random_char(chars[0:length])
    return str


def gen_pwd(length):
    # sample从序列中选择n个随机独立的元素，返回列表
    num = random.sample(src_digits, 1)  # 随机取1位数字
    lower = random.sample(src_uppercase, 1)  # 随机取1位小写字母
    upper = random.sample(src_lowercase, 1)  # 随机取1位大写字母
    special = random.sample(src_special, 1)  # 随机取1位大写字母特殊字符
    other = random.sample(string.ascii_letters + string.digits + string.punctuation, length)  # 随机取4位
    chars = num + lower + upper + special + other
    # shuffle将一个序列中的元素随机打乱，打乱字符串
    str = gen_random_char(chars[0:length])
    return str


def gen100(m, n):
    for i in range(1, n):
        a = random.choice(range(m, m + 5))
        p = random.choice(range(a + 10, a + 15))
        user = gen_user(a)
        pwd = gen_pwd(p)
        if a > 7:
            data = "{}\t{}".format(user, pwd)
        else:
            data = "{}\t\t{}".format(user, pwd)
        print(data)


# 生成100个5-10位随机数
gen100(5, 100)
