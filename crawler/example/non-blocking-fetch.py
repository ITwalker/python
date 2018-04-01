#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 20:09
# @Author  : ljt
# @File    : non-blocking-fetch.py
# @Software: PyCharm
import socket



def non_blocking_send():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('xkcd.com', 80))
    except BlockingIOError:#在非阻塞IO时会出现该错误，该错误是由于IO连接已经存在/正在执行/重复连接等造成的
        pass

    request = 'GET /353/ HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'
    encoded = request.encode('ascii')

    while True:
        try:
            sock.send(encoded)
            break
        except OSError as e:
            pass

    print('sent')

non_blocking_send()

