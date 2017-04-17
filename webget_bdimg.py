#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import itertools
import urllib
import sys
import json
from string import maketrans
import hashlib
from tqdm import trange
from time import sleep

"""
百度图片下载(带进度条)
"""

def decode(url):
    charin ='wkv1ju2it3hs4g5rq6fp7eo8dn9cm0bla'
    charout='abcdefghijklmnopqrstuvw1234567890'
    url = url.replace('_z2C$q',':').replace('_z&e3B','.').replace('AzdH3F','/')
    return url.encode('utf8').translate(maketrans(charin,charout))

if __name__ == '__main__':
    word='python'
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    for url in (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60)):
        html = requests.get(url, timeout=10).content.decode('utf-8') #返回json格式的字符串
        data=json.loads(html)['data']
        for i in trange(len(data)-1):      #进度条
            url=decode(data[i]['objURL'])  #获取图片URL并解码
            urllib.urlretrieve(url,'img/{0}.jpg'.format(hashlib.md5(url).hexdigest())) #下载图片


