import re   # regex  # 파이션에서 정규식을 사용하기 위한 모듈  ## re 정규식 
import requests
urls =['http://www.naver.com','http://www.daum.com']
#for i in range(0,2):
## for문으로 파일을 읽어서 처리가 가능하다. 
## re 소개 
## 문자열 자르기 
## 숫자 
## ip ..
## 파일 저장 
## 3시 10분까지 휴식 하겠습니다.
#ㅁㄴㅇㄻㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇ 777 , 123 1 dfssdfsdf 7777 dsfdfdfdf221323123

#    print("urls[%d]" % (i), urls[i] )
#for  
requests.get('http://www.naver.com').text  
data=re.findall('<span class="ah_k">(.*?)</span>',requests.get('http://www.naver.com').text)[:20]
data=str(data)
data = data +"\n"

f=open('keyword.txt','w')  #  파일설정 , 옵션, w, r, a , b (바이러니)
f.write(str(data))         #  쓰기 
#f.read()                  # 파일읽기
#f.readline()              # 라인별로 읽기
#if os.py                  #
f.close()                  #  받드시 
