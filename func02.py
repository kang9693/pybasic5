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
		
def ex_args3(*args):
	print(*args)
	

_구구단_함수1()
_구구단_함수2()
#_구구단_함수(i=9)
	
	