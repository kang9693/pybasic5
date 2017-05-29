'''
f=open('urls.txt','r')  #  파일설정 , 옵션, w, r, a , b (바이러니)
#f.write(str(data))         #  쓰기 
#line=f.read()     
#print(line)
#f.read())             # 파일읽기
#while <==<
line=f.readline()              # 라인별로 읽기
print(line.strip("\n"))
#if os.py   
              #
f.close()                  #  받드시 
'''
for i in open('urls.txt'):
	i += i.strip("\n")
	#print(i )
	#print(i,end='')
print(i)
## 지금 까지 if, if-else, for , if elif, elif 
##  if elif ## 다중조건 : while  ## 
## open 함수 사용법 
## 파일 읽기 쓰기 #
## 간단하게 응용
## 
###
### 커피자판기 예제 ? 
## if 활용 
#1. 시나리오는

#커피자판기에 커피 10 개 한개의 300원 
# 커피 한개 가격 300원이고 
# 만약 자판기에 400원 넣을때는 잔돈을 체크해서 
# 반환 해주세요. print( " 거름돈 400 -100 거스돈이 100원입니다.)
# 커피 되어야 할까요. ? 차감 .
# 돈을 400번원 넣은 체크 해서  거스름 돈을 내어주는  100
# for 가지고 되는 ?    for 가지고 안된 

coffie=10
coffie_coin= 1000  # 커피 자판기 잔고 
coffe_vul = int(input("커피 가값:"))

if (coffe_vul > 300):
	print( "300원보다 크다.")
	
#name=  str(input())   # 사용법   < ==  
#print("잔고: %d, name:%s" % (잔고,name)) # 포멧스티링  

# while # 
hit=0
#=0

#===============
#'''
if  조건 :

	수행문장 1
	수행문장 2

progam...123123 	
if (): 

else:
	수행문장1
	수행문장2
	수행문장3

#=================
#'''
#while ( hit < 10 ):  # 참일 때 까지 수행 
#	hit = hit + 1 
	#print(" 커피가 %d개 남았습니다." % hit)
#'''	
while True :  # 참일 때 까지 수행   참 11 거짖   # 버그 
                 # Pep8 읽어  True, False 
				 # bool  True 1 
				 # false 0 
					 
	#hit = hit + 1  # 제가   # python 디버깅 곤란 오류 , 버그 
	# 스그 
	hit += 1  ##  권고 하고.   
	print(" 커피가 %d개 남았습니다." % hit)    
	if(hit==110):
		break   # while 구동 멈추는 것 . 


#if (hit == 10
	
	


#'''
##########
#for i range(0,coffe):
	
#if ~ else 
coffe =10
#for i range(0,coffe):
	
# 잔돈이 얼마 있는제 체크 
# 
coffe_vul=300

coin = int(input("커피 가격을 입력해주세요")
########


# 
#100개가 다 팔리면 커피가 없습니다. 라고 출력하는 프로그램 
#만들어 보기 
## 점프투 파이션에 
#10분




############################################# 없음..
#2. if  ~ else 
# Quiz : http://cafe.naver.com/itpysec  여기에  
#과제: 현금 인출기 구현   ( 이번주에 구현 ) 
#1. 잔고 100,000,000
#2. 100만원씩 인출 가능 
#3. 100만원 이하는 인출이 불가능합니다. 
#4. 출금 결과는 화면에 출력 
#5. 로그인시 비밀번호 입력 받기 















