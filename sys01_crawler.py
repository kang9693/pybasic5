## sys01_cralwer.py
##
## python sys01_crawler.py -u http://www.naver.com
import sys
import requests



args = sys.argv[1:]
print(args)

if (args[0]=='-h'):
	r = requests.get(args[1])
	r.status_code	
	print(r.status_code)
	
	###print("인터넷 연결이 안되요.!!!")
