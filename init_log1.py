# -*- coding: utf-8 -*-
# author: itimor

import logging
import os
from sys import version_info


class Log(object):

    def __init__(self, log_path, log_name):
        if not os.path.exists(log_path): os.mkdir(log_path)
        self.log_path = log_path
        self.log_name = log_name
        self.log_full_path = os.path.join(log_path, log_name)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s - %(levelname)s line:%(lineno)d %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        if version_info.major == 3:
            fh = logging.FileHandler(self.log_full_path, 'a', encoding='utf-8') # 这个是python3的
        else:
            fh = logging.FileHandler(self.log_full_path, 'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
