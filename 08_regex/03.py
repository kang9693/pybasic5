import re
import pygeoip
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
pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
i=0
for line in open('access_log'):
	#print(line)
	ip = line.split(' ')[0]  #splite을 이용한 문자열 자르기, 공백으로 구분
	test = pat.match(line)
	re_ip=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",line)
	
	#print (ip,re_ip,test.group())   ### 
	i=i+1
	
	re_ip = re_ip.group()
	
	#import pygeoip
	gi = pygeoip.GeoIP('GeoIP.dat')
	gi.country_name_by_addr(re_ip)
	
	print (ip,re_ip,test.group())   ### 
	
print( 'line count :',i )		

'''
파일로 저장하기 		
#! python
f = open("ip.txt", "w")
for line in open('/var/log/apache2/access.log'):
        ip = line.split(' ')[0]
        f.write(ip + '\n')
f.close()

'''