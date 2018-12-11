#!/usr/bin/python
# encoding:utf-8

import json


data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } 
data['age']=19

jsonstr = json.dumps(data)
print (jsonstr)
jsonobj=json.loads(jsonstr)
#增加成员
jsonobj['name']='zhuang'
print(jsonobj)
