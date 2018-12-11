from urllib import request
from lxml import etree

url="https://bj.lianjia.com/zufang/"
headers={}

req=request.Request(url,headers)
response=request.urlopen(req)
content=response.read().decode()
#html=etree.HTML(content)
#house_list=html.xpath(r'')
print(html)