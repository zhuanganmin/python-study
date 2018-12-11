import tkinter
import sys
# -*- coding: utf-8 -*-

print(sys.path)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import *

top = tkinter.Tk()
li=["c","python","php","html","sql"]
movie=['css','jquery',"bootStrap"]
listb=Listbox(top)
listb2=Listbox(top)
for item in li:
    listb.insert(0,item)
for item in movie:
    listb2.insert(0,item)
listb.pack()    
'put top frame'
listb2.pack()


# 进入消息循环
top.mainloop()