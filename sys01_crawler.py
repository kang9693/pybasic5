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
## 실습하면 5시 15분까지 휴식하겠습니다. 
## 실습하면서 쉬고, 이것을 클래스 구조로 변경 

## 



	###print("인터넷 연결이 안되요.!!!")
