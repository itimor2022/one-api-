# -*- coding: utf-8 -*-
# author: itimor

from datetime import datetime, timedelta
import time


def gen_time_pid(prefix):
    pid = '{}_{}'.format(prefix, datetime.now().strftime('%Y%m%d%H%M%S') + str(time.time()).replace('.', '')[-3:])
    return pid
