class Counter:
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
		
		
class calc(Counter):   	##  calc 자식 클래서 부모 클래스 Counter 라는 클래스에서 상속 받아서 
	pass				#
	
a=calc("IT학원","123-123-123123")
print(a.sum(1,1))