
from Crypto.Cipher import AES
import base64
import this

secret = "12345678912345678912345678912345"             #由用户输入的16位或24位或32位长的初始密码字符串
cipher = AES.new(secret)                                #通过AES处理初始密码字符串，并返回cipher对象
s = cipher.encrypt("1234567891234567")                  #输入需要加密的字符串，注意字符串长度要是16的倍数。16,32,48..
print (s)                                                 #输出加密后的字符串
print (base64.b64encode(s))                               #输出加密后的字符串的base64编码。
print (cipher.decrypt(s))  


