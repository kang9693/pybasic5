#def <=함수를 정의할때 사용 
# filename : title.py
# 파일위치 : lib/title.py
def banner(c):
	a = " 모듈 임포트 하기 연습니다." # 문자열 선언?
	b = " python "
	c=str(c)
	#print(" 모듈 임포트 하기 연습니다.")
	return a,b,c  ## return 반환 하라. 

#함수라는 것 
#1. 결과값을 반환 해주게
#2. 결과값을 반환해 주지 않는것 
def bar():
	prompt="""
		1. 현금인출
		2. 잔고조회
		3. list
		4. Quit
		5. 게임 


		Enter number: """