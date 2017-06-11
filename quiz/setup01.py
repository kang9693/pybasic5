import sys
from cx_Freeze import setup, Executable

## cx_Freeze 를 이용한 컴파일 하는 방법
## py => exe
setup(  name = "name",
        version = "1.0",
        description = "name",
        author = "SeongHun.Kang",
        executables = [Executable("현금인출기.py")])        
		#만약 윈도우 GUI프로그램인 경우 executables의 옵션을 입력해 주어야 한다.
        #executables = [Executable("imgtk.py", base="Win32GUI")])

		
# 실행파일로 만들때 어떻게 		
# 모듈로 인식기 위해서는 __init__.py  만들어 줘야 한다. 
## 윈도우 랑 리눅스/유닉스 동일합니다. 
 
# 내가 만든 모듈을 추가해서 컴파일할때 
# 내가 만든 모듈 경로를 아래와 같이 추가 해준다.
# __init__.py <== 이파일이 있어야 내가 만들 모듈이 python.exe 가 모듈이라고 인식함


# windows 
# 윈도우 CMD 
#set pythonpath="c:\workspace\pybasic5\quiz"	
# set pythonpath="c:\workspace\pybasic5\quiz"  ## 추가로 만든 모듈 에대한 path 경로설정
# unix/linux
# pythonpath="/workspace/pybasic5/quiz"	

## 스크립트 clone 에 등록 하는 방법
## unix/linux 
## /usr/bin/python /workspace/pybasic5/quiz/현금인출기.py   ---- 
## crontab => 특정 시간 작업 주기적 반복 실행하도록 설정하는 리눅스/유닉스 기능 
## "정보보안 기사 <==== "

