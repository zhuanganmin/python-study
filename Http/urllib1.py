#! /usr/bin/python
# encoding=utf-8
# -*- coding: UTF-8 -*-

import urllib.request
import json
#import urllib2 在python3中没有urllib2用urllib.request代替

url="https://httpbin.org"

#get请求
def get(url):
    #发送请求
    response=urllib.request.urlopen(url,None,timeout=3)
    data=response.read().decode()
    jsondata=json.loads(data)
    print(jsondata["args"])
    # fo=open("get.txt","a+",encoding='utf-8')
    # fo.write(data)
    # fo.close()

def post(url,data):
    headers={'Content-Type':'application/json'}
    #创建http请求对象
    request=urllib.request.Request(url,headers=headers,data=json.dumps(data).encode(encoding="utf-8"))
    #发送请求
    response=urllib.request.urlopen(request)
    resultData=response.read().decode()
    return json.loads(resultData)['data']

    pass


if __name__ == "__main__" :
    print("main :")
    get(url+"/get?a=hello")
    data={
        'name':'zhuang',
        'age' : 34
    }
    resultData=post(url+"/post",data)
    print(resultData)


