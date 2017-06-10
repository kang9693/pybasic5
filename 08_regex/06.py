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
soup = BeautifulSoup(plain_text,'lxml')


for link in soup.find_all('a'):
	#print(link.get('href'))           #ranks = soup.find("dl", {"class": "blind"})
	#url_list = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', link.get('href'))
	url_list = re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link.get('href'))
	#mail_list = re.match('\\[^@]+@[^@]+\.[^@]+',link )
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", str(soup))
	emails_1 = re.findall(r"[^@]+@[^@]+\.[^@]+",str(soup))

	if (url_list!=None):	
		print("url:",url_list.group())
		print("mail:",emails)
		print("mail:",emails_1)
		
	else:
		pass
		#print('No data !!')
	#for u in 

