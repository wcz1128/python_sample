#!/usr/bin/python
#coding:utf8
'for my av'
__author__ = 'Hippo'

import re

line="123123uuid=123123#test=111#xxxxx"
#匹配到就结束
print re.findall(".*uuid=(.*?)#.*",line) 
#匹配到最后
print re.findall(".*uuid=(.*)#.*",line) 
