### pybasic5\GUI
### pip install wxpython
### pyQT    <<### GUI 구현제일 활성화  
### pyQT4 << 4 상위   ## pyQT 레이펀스 QT GUI 
### pyQT5 << 5 하위 
### pyt
### wxpython 
### pyside 
### visual msdn 개발참고 사이트    
### 통합된 레퍼런스 사이트가 없다. 
# basic 
#중급 
# 첫 프로그램 기초 입문 
# 데이터 가공 
# 빅데이터 , AI
# 업무자동화 , 마인크래프트 게임 자동  
# 파이션을 이용한 금융공학 
# pykorea www.facebook.com  국내에서 가장 활발한 커뮤니티
# 2달에 1회정도 세미나 
# 
# 
# 질문 메일 또는 카페로 
# kang9693@naver.com 
# cafe:cafe.naver.com/itpysec
# 강성훈 
# Q & A 

# 보안 인공 사용될수 있을까.
## 악성분석 방법론 정형화 
## 정형화 패턴 자동화가 가능해지고 
## fireeye  
## 악성코드 키워드 및 탐지 샘풀의 DB 화 되면서 
## 악성코드도 AI를 이용하여 탐지 및 식별이 가능하다. 
## AI 개발의 보조 같이
## API  

#버그 
### 개발에 대한 접근성 낮아졌다. 
### 개발도 모듈 > 
### 레고 블럭 

# include <sin 





import os
import sys

try:
	import wx
except: 
	os.system("pip install wxpython")   # 상대경로
	                                    # 절대경로 c:\python36\scripts\pip install wxpython
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Char Event Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        btn = wx.TextCtrl(panel, value="")
 
        btn.Bind(wx.EVT_CHAR, self.onCharEvent)
 
    def onCharEvent(self, event):
        keycode = event.GetKeyCode()   ## wxpython 
        controlDown = event.CmdDown()
        altDown = event.AltDown()
        shiftDown = event.ShiftDown()
 
        print (keycode)
        if keycode == 32:
            print ("you pressed the spacebar!")
        elif controlDown and altDown:
            print (keycode)
        event.Skip()
 
 
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm()
    frame.Show()
    app.MainLoop()