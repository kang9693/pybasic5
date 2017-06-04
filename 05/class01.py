###
###
### 사칙연산을 수행하는 계산기 프로그램을 구현해보세요. 
### 1.함수를 이용해서 구현하세요. 
### 2. 연산 값을 각 인자 
### 3. return 값이 있어야 되
### (10분 )
### 
# http://cafe.naver.com/itpysec
# http://www.kmooc.kr  학점 인정 학점 교류가 되는것은 학점인정됨
# https://pyformat.info/  파이션 포멧 스트링  예제 사이트 
## 클래스 class 작성 
## 클래스 
## OOP   객체지향 프로그램 < == 
def sum(a,b):
	return a+b
	
def sub(a,b):
	return a-b
	
def div(a,b):
	return a/b
	
def mul(a,b):
	return a*b
	
a=5
b=2
result=sum(a,b)
print ("sum(%d,%d)=%d" %(a,b,result))
result=sub(a,b)
print("sub(%d,%d)=%d" %(a,b,result))
	


