import re
p = re.compile('[a-z]+')

## 1) ip address check 
## 2) access log 에서 IP 뽑아내기
## 3) access log ip list count 
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