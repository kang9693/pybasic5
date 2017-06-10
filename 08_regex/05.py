import re
import requests
from bs4 import BeautifulSoup

p = re.compile('[a-z]+')

## 1) ip address check 
## 2) access log 에서 IP 뽑아내기
## 3) access log ip list count 
'''
ip="241.1.1.112343434"
#aa=re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]",ip)
#aa.group()


aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip)

if aa:
	ip = aa.group()

print("IP:",ip)

#
#ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip)
#
#print(ip_candidates )
'''
import requests

def url_status_check(url):
	target = url
	r = requests.get(target)
	
	result=r.status_code
	headers = r.headers
	header = r.headers['content-type']
	url = r.url
	json = r.json
	history=r.history
	r.text
	'''
	for i in open("url.txt",'r'):
		#print(i.strip('\n'))
		url = i.strip('\n')
		for reg in open("regs.txt",'r'):
			target=url +"/" + reg.strip('\n')
			print( target )
			r = requests.get(target)
			print(r.status_code)
	'''
	
	return result,url,header,json,history, headers,r.text

	
	
url='http://www.naver.com'
url = url_status_check(url)
#print( url[6] )
plain_text = url[6]
soup = BeautifulSoup(plain_text)
for link in soup.find_all('a'):
	#print(link.get('href'))           #ranks = soup.find("dl", {"class": "blind"})
	#url_list = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', link.get('href'))
	url_list = re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link.get('href'))
	if (url_list!=None):	
		print(url_list.group())
	else:
		pass
		#print('No data !!')
#for u in 

'''
pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")   ### 정규표현식을 정의 한다. 
i=0
for line in open('access_log'):
	#print(line)
	ip = line.split(' ')[0]  #splite을 이용한 문자열 자르기, 공백으로 구분
	test = pat.match(line)
	re_ip=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line) #<==정규식이 잘못 되었을 때
	print ("ip:",ip,"re_ip:",re_ip.group(),"test:",test.group())   ###  # group() 튜플형태로 다운로드 
	
	ip=pat.search(line)
	print("search ip:",ip.group())
	i=i+1
'''
	

	
#print( 'line count :',i )		

'''
파일로 저장하기 		
#! python
f = open("ip.txt", "w")
for line in open('/var/log/apache2/access.log'):
        ip = line.split(' ')[0]
        f.write(ip + '\n')
f.close()

'''