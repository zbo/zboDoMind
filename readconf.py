#!/usr/bin/python
# -*- coding:utf8 -*-

def read():
    dict = {}
    f = open('/home/seluser/zboDoMind/conf','r')
    line = f.readline()
    while line:
       array = line.split('=')
       dict[array[0].strip()] = array[1].strip()
       line = f.readline()  
    f.close()
    return dict

if __name__=='__main__':
    read()