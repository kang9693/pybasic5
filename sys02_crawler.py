## sys01_cralwer.py
##
## python sys01_crawler.py -u http://www.naver.com
import sys
import requests


def https_status_code(url):
	r= requests.get(url)
	r.status_code 
	
	return r.status_code


###print("인터넷 연결이 안되요.!!!")
if __name__ == "__main__":
	
	print(" Usage: \n")
	print("python sys01_crawler.py -u http://www.naver.com")
	#i=input()
	#if not i:break
	sys.argv[1:]  
	#### 
	option=args[0]
	url = args[1]
	if option==' ':
		break
	if option=='-h':
		url_state=https_status_code(url)
	
	