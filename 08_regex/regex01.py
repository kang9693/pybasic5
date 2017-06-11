import re
import pygeoip ## geoip  ## pygetip => ip 국가정보 또는 도시 정보를 매칭 
pat = re.compile("\d")
for line in open('access_log'):
    print(line.split(' ')[0])   # 리스트로 받환된다.  IP만 뽑기위해서는   
	
	
#pip install pygeoip