import requests   ### 
## requests 클래스 
#r=request()
r=requests.get("http://www.naver.com")    # r 객체를 선언한. 
### 웹 페이지 가져오기 => 크로링 
print(type(r))
r.text
#print(r.text)