import os
import sys
import re  ### 정규식 이라는것 이용해서 할꺼입니다. 

#pslist=os.system("tasklist | findstr 현금인출기.exe")
pslist=os.popen("tasklist | findstr 현금인출기.exe") ## command 명령어이용해 실행 결과를 파일로 기록할수 있어요. 
print(type(pslist))
while True:
	line = pslist.readline()
	if not line:break
	#f=open("popen_test.log",'a')
	#pid만 받고 싶다. 이유 프로세스 ID만 알아도 프로그램이 살아 있는지 죽었는지 확인이 가능하다.
	#현금인출기에서 프로그램 구동시 pid를 체크하고 기록해놓고 
	#해당 PID가 존재하는지 검색하여 프로그램 구동상태를 체크한다. 
	#일반적 프로그램 실행 상태 방법론 . 
	## 보안 pid 기록 악성코드 pid 체크 조사.
	## 앞에서 정규식을 이용해서 네이버 인기키워드 해보지 않았나요 ? 
	
	## /tmp/ 
	#print(line.strip("\n"))
	#line=re.findall('\d',line)  
	line=re.findall('\S',line)  
	## 정규식을 이용해서 이런게 원하는 조건에 값을 추출해낼수 있다. 
	
	## 16:05 까지 쉬시면서 pid만 추출이 가능하도록 수정해보세요
	## 슬라이스와 정규식 숫자만 뽑는것을 이용해야 합니다. 
	
	
	pid만 받고 싶다. 
	# 4시 5분까지 쉬면서 구현해보세요
	
	#'\d' <== 의미 숫자만 출력해/ 
	
	#문자만 구분해줘 
	#'\S'
	print(line)
	### 
	
	#print(line.strip("\n"))  ###  pid 를 확인해서 처리고 싶다. 
	                         ### pid  프로세스 IDP
							 ### pid  프로세스 관리, 클래스 부모 클래스  
							 ### 부모클래스  pid 
							 ### ppid  부모프로세스    프로세스 관계에도 상속 관계가 있습니다. 
							 ### ppid, pid 
	### 여기에서 
	#f.write(line.strip("\n"))
	#f.close
	
	# 코드사인   프로그램 배포 서명 => 악성의심 