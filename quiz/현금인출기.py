import os
#통장잔고= 


banner="""

			코리아 IT 현금 인출기 입니다.!!!
			비밀번호 누출에 주의해 주세요.!!!
            ( 어깨넘어로 처다 보기 주의  !!!)

    """

prompt="""
	1. 잔고조회
	2. 현금인출
	3. 현금입금
	4. 계좌이체
	0. 프로그램종료
	"""

#num = int(input())

while True:
	os.system("cls")
	print(prompt)
	print("==="*5,"코리아 IT 현금일출기 입니다. ", "==="*5)
	print(prompt)
	num = int(input('메뉴를 고르세요'))
	if(num == 0):
		break 
		
	passwd = str(input('비밀번호(노출주의):'))
	
	print(len(passwd))
	if num == 1:
		print("잔고조회")
		
		
	elif num == 2:
		print("현금인출")
		
	#elif num == 0:
	#	print("프로그램 종료 ")
	#	break