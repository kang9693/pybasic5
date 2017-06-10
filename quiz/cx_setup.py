import sys
from cx_Freeze import setup, Executable


#includes = ['lib']
path = ['__lib']
setup(  name = "현금인출기",
		
        version = "0.1",
        description = "현금인출기",
        author = "SeongHun.Kang",
		#options={"build_exe":{"includes":includes}},
		#options={"build_exe":{"path":path}},
		
        executables = [Executable("현금인출기.py")])        
		#만약 윈도우 GUI프로그램인 경우 executables의 옵션을 입력해 주어야 한다.
        #executables = [Executable("imgtk.py", base="Win32GUI")])


