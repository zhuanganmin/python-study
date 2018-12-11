
import crypt
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# -*- coding: UTF-8 -*-

def testPass(cryptPass):
 
	#dictfile=open('dictionary.txt','r')
	start_index=cryptPass.find("$")
	finish_index=cryptPass.rfind("$")
	salt=cryptPass[start_index:finish_index+1]
 
	try:
		dictfile=open(sys.argv[2],'r')
	except Exception:
		print ("Error ! "+str(Exception))
		exit(0)
 
	for word in dictfile.readlines():
		word=word.strip('\n')
		cryptWord=crypt.crypt(word,salt)
		if cryptWord==cryptPass:
			print( "[+] Found Password: " +word+ " \n")
			return
	print('[-] Password not found!')
	return
 
def main():
 
	if len(sys.argv)==3:
		try:
			shadowfile=open(sys.argv[1])
		except Exception:
			print ("Error !" +str(Exception))
			exit(0)
	else:
		print("Usage:python ShadowCracker.py [shadow file] [dictionary file]")
		exit(0)
 
	passfile=open('passwords.txt','r')
 
	for line in passfile.readlines():
		user=line.split(':')[0]
		cryptPass=line.split(':')[1].strip('\n')
		print ("[*] Cracking Password For: " +user)
		testPass(cryptPass)
 
if __name__=='__main__':
    main()