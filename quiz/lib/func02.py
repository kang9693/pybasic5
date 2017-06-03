### 구구단을 구하는 함수를 만드세요. ###  
### 숫자를 입력받아서 해당 구구단을 출력하는 프로그램을 작성하세요.
### 함수로 구현 하세요. 
### for문을 사용. 
### 10분간 해보세요. 
### 

def _구구단_함수1(num=9):
	#=0
	for i in range(1,10):
		print("\t",i,num,i*num)   ## 여기서 ","는 공백 한칸을 띄우는 의미 

def _구구단_함수2(num=9):
	#=0
	for i in range(1,10):
		print("%d * %d = %d" %(i,num,i*num))
			
		#print("%d * %d = %d" % (i,num,i*num))

#입력값이 몇개가 될지 모를때
def ex_args3(**args):   ### args 
	print(args)
	sum=0
	for i in args:
		sum = sum+i    ## *args에 입력받은 모든 값을 더한다.
	return sum
def ex_test2(a,b):   ### args  # 함수의 인자 전달
	for i in range(a,b):
		print(i)
		
def ex_test3(a,b):  
	while True:
		#i=a
		print(a)
		a= a+1
		#print(a)
		if( a >=b):break
		
		#if(b >=a
def ex_args4(*args):   ### args 
	print(args)
	'''
	'sum=0
	for i in args:
		sum = sum+i    ## *args에 입력받은 모든 값을 더한다.
	return sum
	'''

	
ex_args4(1,2,3,4,5,6,7,8,9,10)
## 프로그램 함수?

def file_write()
	
## 단기능 을 구현사용 사용하는것 ?
## 기능을 구현해서 재사용하기 위해서 함수를 만드다. 


## 
## 프로그램 실행 결과를 기록 하고 싶다 ?
## 어떻게?



#print()
#range() 함수 로 만들어 진것을 가져더 사용 
# 수익률, 증가율, 증감율, 함수 return

## 주말해 보세요!!!
## 현금인출기 프로그램을 함수 구조로 변경 할수 있을까요 ? !!!
## 현금인출기 프로그램을 함수 구조로 변경해서 cafe에 올려주세요.
## cafe.naver.com/itpysec  

for i in range(10):
    print(i, end=" ")












	