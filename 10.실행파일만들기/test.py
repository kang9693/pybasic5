import sys
from cx_Freeze import setup, Executable

setup(  name = "name",
        version = "1.0",
        description = "name",
        author = "SeongHun.Kang",
        executables = [Executable("현금인출기.py")])        
		#만약 윈도우 GUI프로그램인 경우 executables의 옵션을 입력해 주어야 한다.
        #executables = [Executable("imgtk.py", base="Win32GUI")])

### 본인 이름이 출려되는 실행 파일을 
### 내가 프로그램을 누군가에게 제공 하다면 .py 
### python 설치 안되어 있다.
### exe . 
### 
### 본인 이름이 출력되는 실행파일 


예외처리
#
#print("" ) python 3.X
#print " " python 2.X 