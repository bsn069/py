#!/usr/bin/env python
#encoding: utf-8
 
 
from urllib import request
import re
import sys  
 
 
def getSelfIP():
    with request.urlopen('http://www.baidu.com/baidu?wd=ip') as f:
        data = f.read().decode('utf-8')
        # print('Status:', f.status, f.reason)
        result = re.search(r'我的ip地址(\d+\.\d+\.\d+\.\d+)\s+属于(\w+)\s+', data)
        # print(result)
        ip = result.group(1)
        addr = result.group(2)
        print(ip, addr)


if __name__ == '__main__':
    getSelfIP()
 