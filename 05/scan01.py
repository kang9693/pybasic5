## sys01_cralwer.py
##
## python sys01_crawler.py -u http://www.naver.com
## 외부 인자. 
import sys
import requests

#a = input("!@#!@#")
args = sys.argv[1]  ## python 스크립트 외부에서 받는 것 방법  외부인자.
print(args)
################################
if (args[0]=='-h'):
	r = requests.get(args[1])
	r.status_code	
	print(r.status_code)
