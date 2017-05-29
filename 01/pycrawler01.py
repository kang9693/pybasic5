import requests
#import bs4 
#리스트  합치기
# += 증감 연산자  <=  프로그램에서 이런형 , 축약  
# 
urls = ['http://www.naver.com','http://www.daum.net']
urls += ['http://www.boannews.com'] 
urls += ['http://www.google.com']
urls += ['http://www.facebook.com']

# website: port 80 < ==>  접속 체널 같은 것 
#urls = urls + urls1 + urls2
# 리스트 더하기 
for url in urls:
	r = requests.get(url)
	r.status_code
	r.text 
	print(r.text) 	
	
	print("site Url:" + " " + url + "," + "Site Status:"+" "+ r.status_code )
	print("site Url: %s, site status: %s" %(url,r.status_code))
	
	# [1-9]-[1-9]
	
	
	# 과제 1 이것으로 http에 대해서 상태 를 체크 하고 파일로 저장 하는 
	# 프로그램을 작성 해보세요. 
	# 파일의 형태를 텍스트 파일로 저장 하기 
	
	
	'''
	f = open('text.txt','w')
	## .write(,,,
	## f.close())
	#while for   while 또같이  \
	# for문  정해진 구간을 반복
	# while문 조건이 만족될 때 까지 반복
	
	if ( 200 == r.status_code):
		print("site Url: %s, site status: %s" %(url,r.status_code))
	else:
		print( " site Url: %s, Site status: %s" %(url,"site bad check"))
	'''
