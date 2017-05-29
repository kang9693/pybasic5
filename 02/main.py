########
# 파일위치 : c:\workspace\py_5m\pybasic5\02\
# main.py
# 

from lib import title  # 사용법 1  title.py 있는 함수만 가져와라
from lib import *      # 사용법 2  lib 아래의 모든것을 가져와라.
## 함수를 내가 만들어 계속 재사하는 방법 
## 함수를 만들 , 내가 만든 함수를 가져오는 방법 
## 
##
## 
# 함수 포인토 

#title.py 안에 있는 함수를 가져옴
#a= title.banner(5)
#print(a)
#main1, ma3 
#banner. gmit. 시랳ㅇ 함수 
#void main(){
#
#}
	


def main():	  # def 함수 선언 / 변수 선언 다른것이다.  ## 약속 main() 프로그램 시작 부분이다. 구동부 
              # 함수 기능 집합 
			  # 클래스  함수들의 집합 
	a= title.banner()
	print(a)
	
###	# 함수를 가져다 쓴것이다.

if __main__="__main__":  ## 항상 이된다. 
	main()               # 파이션 인터프린터 가 구동할때 다른 함수가 참조 하는지 않하는지
	
