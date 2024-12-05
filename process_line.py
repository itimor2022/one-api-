# -*- coding: utf-8 -*-
# author: itimor

import time
import secrets


def process_line():
    scale = 100
    for i in range(scale + 1):
        a = '#' * i
        b = "-" * (scale - i)
        c = (i / scale) * 100

        # \r是光标退回行首，end=""防止换行，就可以让后面的输出覆盖前面的
        # 左边以3个格子为大小，^表示让百分数居中对齐，整体设置3个槽位{}
        if i == 100:
            print("\r注入能量 [{}{}] {:^3.0f}% \r\n".format(a, b, c), end="")
        else:
            print("\r注入能量 [{}->{}] {:^3.0f}% ".format(a, b, c), end="")
        t = secrets.choice([0.1, 0.5, 0.7, 1, 0.3])
        time.sleep(t)


process_line()
