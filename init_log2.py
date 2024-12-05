# -*- coding: utf-8 -*-
# author: itimor

import logging
import os
from sys import version_info


class Log(object):
    def __init__(self, log_path='/tmp', log_name='fuck.log', log_level='DEBUG'):
        if not os.path.exists(log_path): os.mkdir(log_path)
        self.__path = os.path.join(log_path, log_name)
        self.__level = log_level
        self.__logger = logging.getLogger()
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        if version_info.major == 3:
            file_handler = logging.FileHandler(self.__path, 'a', encoding='utf-8')  # 这个是python3的
        else:
            file_handler = logging.FileHandler(self.__path, 'a')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        # fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
        # datefmt = "%a %d %b %Y %H:%M:%S"
        fmt = "%(asctime)-5s %(levelname)s %(module)s %(lineno)d %(message)s"
        datefmt = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回looger"""
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger


if __name__ == '__main__':
    log = Log()
    logger = log.Logger
    logger.debug('I am a debug message')
    logger.info('I am a info message')
    logger.warning('I am a warning message')
    logger.error('I am a error message')
    logger.critical('I am a critical message')
