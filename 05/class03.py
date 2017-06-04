
### Programmer 
### 클래스 사용했을때 장점 
### 1. 함수를 재사용할수 있다.
### 2. 은닉화(데이터를 처리과정을 숨길수 있다)

## 가장 간단한 클래스를 만든것 
## 
#class Tetris(wx.Frame):        
#class 클래스(부모클래스):
class Programmer:
	#print("강성훈입니다.!!!")
	#def __init__
	secret = "영구는 배꼽이 두 개다."
	## 기본값을 선언하는 방법
	def __init__(self, name,계좌번호):        ### __init__   "객체를 만들 때 항상 실행된다."
		self.name = name             ### 클래스에서 반드시 이값을 받아야 한다. 
		self.계좌번호=계좌번호
		
		
	def aa(self):                      ## 파이션의 문법 
		print("test test") 
	def sum(self,a, b):                # 더하기 서비스
		result = a + b
		print("%s + %s = %s입니다." % (a, b, result))
		return result
		secret = "영구는 배꼽이 두 개다."
	def sub(self, a, b):                # 더하기 서비스  ## class 접근하는 객체 자기자신이에요.
		result = a - b
		print("%s - %s = %s입니다." % (a, b, result))
		return result
	def mul():
		result = a*b
		return result
	#pass   
	#pass   
	#self.
#class HouseKim(Programmer):
#    lastname = "김"
#================================#

#클래스 상속 이된다.  
class Test(Programmer):     ## 자식클래스(부모클래스) =>  상속 클래스 
    lastname='김'

Hun= Test("강성훈","123-123-123123")   # 자식클래스에 대한 객체 선언해 부모클래스를 접근할수 있다. 
#Hun.as()

print(Hun.name,Hun.계좌번호)
Hun.aa()


##!!!계산기 클래스를 만들고  계산기 기능을 상속 받는
##  cacl 자식클래스를 생성하여 접근해 보세요.   
## 15 분

git commit 

### 어떻장점 ? 


### 내가 쓰고 함수 가져 있다. 다른사람 
### dll  동적라이브러 API 가져다 쓸수 있다.    ## 함수 이름 전달 메시지 구조 
### 은닉화   숨기는 구체적 기능 숨기는게 가능하다. 


##kim = Programmer("강성훈","123-123-123123")   ## kim 객체     kim객체
##print(kim.name,kim.계좌번호)
##park =  Programmer("강현우","999-9999-99999")   ## park 객체 객체 
##print(park.name,park.계좌번호)
## print(type(park.name))





## 4시 10분까지 쉬면서 실습해보세요 .

#즉 클래스에서 만 객체가 선언 되고 객체로 클래스내 변수가 접근 가능
# 기능 접근 가능 ..
#print(kim.secret, park.secret)
#print(Programmer.secret)
#kim.sum(1,1)
#ssum = kim + park
#print(d)
#print(ssum)
#park.sub(1,1)
#Programmer.aa(park)
#park
#kim


#print(type(kim))
#print(type(park))


'''
def sum():
	asecret = "영구는 배꼽이 두 개다."
	#print("강성훈입니다.:")
	
a=sum()   ## 객체 선언   안됨 
b=sum()   ## 객체 선언   안됨 
print( a.asecret,b.asecret)
#print(type(a))
#print(type(b))
'''


