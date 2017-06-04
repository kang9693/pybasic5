###
###
### 사칙연산을 수행하는 계산기 프로그램을 구현해보세요. 
### 1.함수를 이용해서 구현하세요. 
### 2. 연산 값을 각 인자 
### 3. return 값이 있어야 되
### (10분 )
### 
### class 함수들의 집합니다. 
# http://cafe.naver.com/itpysec
# http://www.kmooc.kr  학점 인정 학점 교류가 되는것은 학점인정됨
class Calculator:    
	
	#self.num1='네임'
	#self.num2='123123'
	def add(self,num,num2):   ## self < 파이션 만 있는것 ?  self 자기자신 
		result = num + num2
		print(result)
		return result
		
	def sub(self, num, num2):     ## 메소드 
		result = num - num2
		return num-num2
		#print(result)

	def multiply(self,num,num2):
		result = num * num2
		return num-num2
		#print(result)

	def divide(self,num,num2):
		if num ==0 or num2 == 0:
			print("Error")
			return
		result = num / num2
		return result 

calc1=Calculator()   ## 인스턴드 선언 
calc2 = Calculator()
calc1.add(1,1)       ## 
calc2.add(1,1)
calc1.sub(1,1)    ## calc1 인스턴드 sub 메소드 접근하고,. 메세지(1,1) 
f=open('../quiz/log.txt','r')  #객체 선언   class()
print(type(f))
f.close()



	


		



