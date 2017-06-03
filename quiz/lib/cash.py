

def Cash_withdrawal(name,Account_Number,money):
	#while True:
	os.system('cls')
	banner="===="*5+"===="*5+"==="*5+"==="*5+"===="+"\n"	
	banner=banner+"===="*5+" "+"현금인출기 잔고 조회 화면입니다. "+"===="*5+"\n"
	banner=banner + ("1. %s 님 잔고조회 입니다. " % name )	
	print(banner)
	
	banner="\n"+ banner+ ("""
			예금주명 %s
			계좌번호 %s
			계좌잔고 %d
			""" % (name,Account_Number,money))
						
	print(banner)
	#enter=input()	
	#enter=input()
	#if not enter:
	#	break
			
	#return banner