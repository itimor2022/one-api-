# -*- coding: utf-8 -*-
# author: timor

from datetime import datetime, timedelta
import time
import pygame
import sys


def utc2local(utc_st):
    """
    UTC时间转本地时间 +8:00
    """
    now_stamp = time.time()
    local_time = datetime.fromtimestamp(now_stamp)
    utc_time = datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def local2utc(local_st):
    """
    本地时间转UTC时间 -8:00
    """
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.utcfromtimestamp(time_struct)
    return utc_st


# '2015-08-28 16:43:37.283' --> 1440751417.283
# 或者 '2015-08-28 16:43:37' --> 1440751417.0
def string2timestamp(strValue):
    try:
        d = datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S.%f")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000
        return int(timeStamp)
    except ValueError as e:
        d = datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000
        return int(timeStamp)


# 1440751417.283 --> '2015-08-28 16:43:37.283'
def timestamp2string(timeStamp):
    try:
        d = datetime.fromtimestamp(timeStamp)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
        # 2015-08-28 16:43:37.283000'
        return str1
    except Exception as e:
        pass


def sound_notice():
    pygame.init()
    pygame.mixer.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption('大家好,我是胖头鱼王 "冰冰"')
    bg = pygame.image.load("bingbing3.jpg")
    screen.blit(pygame.transform.scale(bg, size), (0, 0))
    pygame.display.update()
    mp3 = 'test.mp3'
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        music_status = pygame.mixer.music.get_busy()
        if not music_status:
            sys.exit()


def spent_time(func):
    def inner(*args, **kw):
        print(f'开始喽...')
        start_time = datetime.now()
        func(*args, **kw)
        end_time = datetime.now()
        s = int((end_time - start_time).seconds)
        if s > 60:
            total_time = f"总共花费时间 {int(s / 60)}分{s % 60}秒"
        else:
            total_time = f"总共花费时间 {s} 秒"
        sound_notice()
        print(f'结束辣...')
        print(total_time)

    return inner


if __name__ == '__main__':
    sound_notice()
