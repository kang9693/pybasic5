import os
import time

###########################################
from lib import log
from lib import banner
from lib import menu
#from lib.banner import *

#p()	
#a=banner()
#print(a.banner())


#num = int(input())
money=1000000 ## 통장잔고 
name = '홍길동'  ## 예금주명
Account_Number='123-456-7890'
Cash_withdrawal=0 # 인출금액

while True:
	os.system('cls')  	### DOS 명령어 CLS 명령어 수행
	#print(banner)  	### 함수 위치 
	banner.front_banner()	
	enter = input("현금인출기를 시작 할려면 엔터를 입력해주세요!!!(Q는 현금인출기종료): ")
		
	if(enter=='Q'):
		os.system('cls')
		banner.ending_banner()
		break
	#else:
	#	print("")

	
	if not enter:
		while True:
			
			
			#@goto
			os.system('cls')
			print("===="*5,"===="*5,"==="*5,"==="*5)
			print("===="*5,"코리아 IT 현금일출기 입니다. ", "===="*5)
			menu.prompt()
			#print( prompt )
		
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
				
				
					if(num == 2):
						print("===="*5,"===="*5,"==="*5,"==="*5)
						print("===="*5,"현금인출기 잔고 조회 화면입니다. ", "===="*5)
						print("\n")
						print("2. %d 님 인출가능금액 입니다. " % money )
						print("\n")
						print("인출금액을입력해주세요!!!")
						Cash_withdrawal=int(input(">>>"))
						
						if ( Cash_withdrawal > money ):
							print("잔고가 부족합니다. !!!")
						
						if( Cash_withdrawal < 10000 ):
							print("10000원 인출이 불가능합니다.")
						
						elif(Cash_withdrawal >= 10000):
							print(" %d원 을 인출 하시겠습니다.!!! " % Cash_withdrawal )
							q = str(input("인출(Y), 취소(N)::"))
							if(q=='Y' or q=='y'):
								money = money - Cash_withdrawal
								print(" %d 원 금액을 인출 하시겠습니다.!!! " % Cash_withdrawal )
								print("잔고 %d원 입니다. .!!! " % money )
								
							if(q=='N' or q=='n'):
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

		
	
