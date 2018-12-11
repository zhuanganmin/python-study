#!/usr/bin/python
#encoding: utf-8
import requests
import json

url="http://httpbin.org/post"

def putfile(url,data,file):
    data['enctype']='multipart/form-data'
    return requests.post(url,data,file)


if __name__ == "__main__":
    print('main:')
    file={'image':open("C:\\ren.jpg",'rb')}
    data={'name': 'zhuang'}
    response=putfile(url,data,file)
    print(response.text)
    # data={''}
    # putfile()
