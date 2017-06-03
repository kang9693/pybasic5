import os    ### os 시스템 관련된 명령어 및 기능을 사용할때 
import time
from lib import log
#import
#통장잔고= 
######################################################
def banner():   ## 이거 입력 인수 함수 
	## tab 4
	banner="""
			

			
			코리아 IT 현금 인출기 입니다.!!!
			
			
			>>> 아무키나 입력해주세요!! <<<
			
			

    """
	print( banner ) 
	#result = banner
	#return result
########################################################

#def 함수명(입력인수):   ## 함수 명은 프로그램머가 정하는것이다. 단 규칙에 따라. 
						 ## PEP 함수 명에 대한 작성 규칙 규칙 작성한다. 
						 #
						 # 
#    수행할 문장1
#    수행할 문장2

a= banner()   ## 이런게 작성하는 것을 객체 선언이라고 합니다.
#print(a)


prompt="""
	1. 잔고조회
	2. 현금인출
	3. 현금입금
	4. 계좌이체
	0. 프로그램종료
	"""
passwd='1234'
passwd_count=0
#num = int(input())
money=1000000 ## 통장잔고 
name = '홍길동'  ## 예금주명
Account_Number='123-456-7890'
Cash_withdrawal=0 # 인출금액

while True:
	os.system('cls')   ## 시스템 명령어
	print(banner)
	enter = input("엔터를 입력해주세요!!!(Q는 현금인출기종료): ")
		
	if(enter=='Q'):
		break
	
	if not enter:
	
	#if (passwd='1234'):
	
	
		while True:
			
			
			#@goto
			os.system('cls')### 시스템 명령 
			print("===="*5,"===="*5,"==="*5,"==="*5)
			print("===="*5,"코리아 IT 현금일출기 입니다. ", "===="*5)
			print( prompt )
		
			num=int(input("메뉴를 선택해주세요.!!:>>>>"))
			
			if(num!=''):
				print('%d' %num )
			
			#num = int(num)
			if( num == 0):
				break				
			
			
			'''
			if(num == 1):
				print("1. 잔고조회 입니다. ")	
				print("While loop has exited")
			'''
			if (num !=''):
				##### 패스워드 체크
				while True:
					os.system('cls')
					#enter=input()
					
					if(num == 1):
						passwd=str(input("패스워드입력해주세요:"))
						if ( passwd=='1234'):							
							if(passwd_count==5):break  ## 							
							print("===="*5,"===="*5,"==="*5,"==="*5)
							print("===="*5,"현금인출기 잔고 조회 화면입니다. ", "===="*5)
							print("1. %s 님 잔고조회 입니다. " % name )	
							print( """
								예금주명 %s
								계좌번호 %s
								계좌잔고 %d
							"""% (name,Account_Number,money))
							
							enter=input()
							
							if not enter:
								break
						else:
							print("패스워드 들린회수: %d" % passwd_count)
							passwd_count=passwd_count+1
							#print(pas
							
				
				
					if(num == 2):
						print("===="*5,"===="*5,"==="*5,"==="*5)
						print("===="*5,"현금인출기 잔고 조회 화면입니다. ", "===="*5)
						print("\n")
						print("2. %d 님 인출가능금액 입니다. " % money )
						print("\n")
						try:  	  #예외처리 구분 
							print("인출금액을입력해주세요!!!")
							Cash_withdrawal=int(input(">>>"))
						except ValueError as e:  ## 에러 상황 발생하면 아래구간이 
							meg = time.strftime("%B %d %Y")+" "+"ValueError: %s" %e 
							log.log_write('log.txt',meg,'a')
						#ValueError: invalid literal for int() with base 10: ''
							print("입력값이 없습니다. 다시 입력해주세요!!!")

						
						if ( Cash_withdrawal > money ):
							meg=time.strftime("%B %d %Y")+" "+ "잔고가 부족합니다."	
								#time.strftime("%B %d %Y")						
							print("잔고가 부족합니다. !!!")
							log.log_write('log.txt',meg,'a')   ## a 파일 인출기록 계속 추가해야하니까.
							
						
						if( Cash_withdrawal < 10000 ):
	
							print("10000원 인출이 불가능합니다.")
							meg=time.strftime("%B %d %Y")+ " " + "10000원 인출이 불가능합니다."
							log.log_write('log.txt',meg,'a')  ## a 생각하는데
						## logging 모듈 
						elif(Cash_withdrawal >= 10000):
							try:  					
								print(" %d원 을 인출 하시겠습니다.!!! " % Cash_withdrawal )
							except:
								print("입력이 정확하지 않습니다.!!!")
							q = str(input("인출(Y/y), 취소(N/n):"))
							if(q=='Y' or q=='y'):
								money = money - Cash_withdrawal
								print(" %d 원 금액을 인출 하시겠습니다.!!! " % Cash_withdrawal )
								print("잔고 %d원 입니다. .!!! " % money )
								#| 파이라인 or
							if(q=='N'or q=='n'): # ||(or연산) y 도 되고 Y 된다.  && (and) 
								break
						
						
							
						enter=input("아무키나 입력해주세요.")
						if not enter:
							print("감사합니다.!!! ")
							break
				
					if(num == 3):		
						print("===="*5,"===="*5,"==="*5,"==="*5)
						print("===="*5,"현금인출기 잔고 조회 화면입니다. ", "===="*5)
						print("\n")
						#print("1. %d 님 인출가능금액 입니다. " % money )
						print("3. 현금입금금액 입력해주세요!!!")							
						Cash_deposit=int(input(">>>"))
						money = money + Cash_deposit						
						
						enter=input("아무키나 입력해주세요 !!! ")
						
						if not enter:
							print("이용해주셔서 감사합니다.!!!")
							break
					
					if(num == 4):
						print("4. 계좌이체 메뉴입니다.")
						print("이용준비중입니다. 감사합니다...")
						enter=input()
						
						
						if not enter:								
							break
			else:
				pass
			''''''
		
	
	
	#elif(enter==0):
	#	break
		
	
	#4. 계좌이체
	
	
	
	#else:
		
	
	
	#input()
	#while True:
	#	i = input("Enter text (or Enter to quit): ")
	#	if not i:
	#		break
	#	print("Your input:", i)
	#print("While loop has exited")
	
	'''
	os.system("cls")  
	#print()
	print(banner)
	sleep('5')
	os.system("cls")  
	print('\n')
	print('\n')
	print('\n')
	print("===="*5,"===="*5,"==="*5,"==="*5)
	print("===="*5,"코리아 IT 현금일출기 입니다. ", "===="*5)
	print(prompt)
	num = int(input('메뉴를 고르세요:'))
	if(num == 0):
		break 
		
	passwd=input('비밀번호(노출주의):')
	#if( )	

	if(passwd=='1234'):
		#print(len(passwd))
		#os.system("cls") 
		if num == 1:
			print("===="*5,"===="*5,"==="*5,"==="*5)
			print("===="*5,"코리아 IT 현금인출기 잔고조회 메뉴입니다. ", "===="*5)
			print("잔고조회")	
			
		
		elif num == 2:
			print("현금인출")
	else:
		print("패스워드가 틀렸습니다.!!!")
	#elif num == 0:
	#	print("프로그램 종료 ")
	#	break
	'''