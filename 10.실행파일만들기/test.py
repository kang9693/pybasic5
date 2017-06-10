import sys
from cx_Freeze import setup, Executable

setup(  name = "parser",
        version = "1.0",
        description = "Parser",
        author = "SeongHun.Kang",
        executables = [Executable("exe01.py")])        
		#만약 윈도우 GUI프로그램인 경우 executables의 옵션을 입력해 주어야 한다.
        #executables = [Executable("imgtk.py", base="Win32GUI")])


