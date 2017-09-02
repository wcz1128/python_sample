#!/usr/bin/python
#coding:utf8
'for my av'
__author__ = 'Hippo'

import socket
import threading
import time

def tcp_send():
    time.sleep(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8880))
    s.send("this is tcp test")
    data = s.recv(1024)
    print data
    s.close()

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    data = sock.recv(1024)
    sock.send(data)
    sock.close()

t_send=threading.Thread(target=tcp_send, name='LoopThread')
t_send.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8880))
s.listen(5)
sock, addr = s.accept()
threading.Thread(target=tcplink, args=(sock, addr)).start()

s.close()
