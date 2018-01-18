# -*- coding:utf-8 -*-

import requests
import os

PHONE_ATTR_PATH = """http://api.k780.com:88/?app=phone.get&phone="""

def getZone(phone):
    path1 = "http://api.k780.com:88/?app=phone.get&phone="

    path2_test = "&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json"

    res = requests.get(path1 + phone + path2_test)
    print(res.json())
    json_str = res.json()
    json_result = json_str['result']
    json_area = json_result['area']
    print(json_area)
    fname = json_area + '.txt'

    if os.path.exists(fname):
        f = open(fname, 'a')
        f.write(phone)
        f.close()
    else:
        print('file not exists!')
        f = open(fname, 'w')
        f.write(phone)
        f.close()

f = open("phones.txt")
line = f.readline()
while line:
    print(line)
    if line.strip():
        getZone(line)
    line = f.readline()
f.close()
