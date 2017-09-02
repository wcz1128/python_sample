#!/usr/bin/python
#coding:utf8
'for my av'
__author__ = 'Hippo'

import socket
import threading
import time

def udp_recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9999))
    data, addr = s.recvfrom(1024)
    print data,addr
    s.close()



t_recv=threading.Thread(target=udp_recv, name='LoopThread')
t_recv.start()

time.sleep(2)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("this is test", ('127.0.0.1', 9999))
s.close()

t_recv.join()
