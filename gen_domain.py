# -*- coding: utf-8 -*-
# author: itimor

import random
import string


def gen_web(site):
    for i in range(10):
        num = string.ascii_lowercase + string.digits
        hou = "".join(random.sample(num, 3))
        full_site = f'{site}{hou}.space\t\tweb.{site}{hou}.space'
        print(full_site)


def gen_landing(site):
    n = 11

    for i in range(n, n + 10):
        full_site = f'{site}store{i}.space\tlanding.{site}store{i}.space'
        print(full_site)


if __name__ == '__main__':
    site = 'b2bxq'
    gen_web(site)
    gen_landing(site)
