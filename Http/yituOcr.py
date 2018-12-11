#!/usr/bin/python
# encoding: utf-8
import json
import requests
import base64
from tkinter import *
from tkinter import messagebox,filedialog


url="http://172.16.3.183:8080/OcrWeb/servlet/OcrServlet"

def ocr(url,image):
    with open(image,'rb') as f:
        image=f.read()
        f.close()
    data={
        'filedata':base64.b64encode(image),
        'pid': 2
    }
    return requests.post(url,data)

def openfile():
    file=filedialog.askopenfilename()
    res=ocr(url,file)
    print(file)
    print(res.text)
    listb.insert(INSERT,res.text)
    

if __name__ == "__main__":
    root=Tk()
    root.geometry("600x400")
    root.title("OCR Test")
    btn1=Button(root,text="选择身份证文件",command=openfile)
    btn1.pack()
    listb=Text(root)
    listb.pack()

    root.mainloop()