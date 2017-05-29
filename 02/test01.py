prompt="""
1. 현금인출
2. 잔고조회
3. list
4. Quit
5. 게임 


Enter number: """

number = 0
while number != 4:   ### ! 부정  4 하고 같지 않으면 
	print(prompt)
	number =int(input())
	if (number == 1):
		print("현금인출")
		passwd=input("비밀번호를 입력해주세요")
	if ( number == 5):    ## ==, !=, >= , <= 비교연산자,   비교 기준 왼쪽 변수, 오른쪽 비교하는 값 오는것. 
		prompt="""
		1. RPG
		3. Tetris
		3. 슈팅게임
		6. Quit   
		Enter number: """
	while True:                         ### 방금보면 : while while 쓸수 있어.    그리고 break 빠져나오기 인데.. if 단독으로는 안되요. while 안에서만. 
										### break 특정 조건 강제로 빠져오는것 
		print(prompt)
		number =int(input())
		if( number==6):
			break
	
	print("erer")