
import wx
import random

class Tetris(wx.Frame):
    
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(180, 380))
        
		self.initFrame()
    
	def initFrame(self):

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText('0')
		self.board = Board(self)   ## 게임관련 보드 
		
		#self.board.SetFocus()
		#self.board.start()

		#self.Centre()
		self.Show(True)
      
class Board(wx.Panel):              # Tetris Board 초기화 
    
	
	BoardWidth = 10   	## 	보드 폭  선언
	BoardHeight = 22  	## 	보드 높이 선언
	Speed = 300    		### 게임속도
	ID_TIMER = 1
	
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		
		
	def initBoard(self):  
		self.timer = wx.Timer(self, Board.ID_TIMER)
		self.isWaitingAfterLine = False
		
		self.curPiece = Shape()   #
		self.nextPiece = Shape()  #  
		
		
		
		self.curX = 0                   ###
		self.curY = 0                   ###
		self.numLinesRemoved = 0
		self.board = []
        
		
		self.isStarted = False
		self.isPaused = False

		self.Bind(wx.EVT_PAINT, self.OnPaint)   
		self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)    ### 키 컨트롤
		self.Bind(wx.EVT_TIMER, self.OnTimer, id=Board.ID_TIMER)
		
	def shapeAt(self, x, y):
		#debug_log("(y * Board.BoardWidth) + x:",(y * Board.BoardWidth) + x)
		x=int(x)
		return self.board[(y * Board.BoardWidth) + x]   ## 보더 폭 사이즈 제어 		

	def setShapeAt(self, x, y, shape):
		x=int(x)        
		self.board[(y * Board.BoardWidth) + x] = shape
	
	## 블럭의 크기 제어
	def squareWidth(self):
        
		return self.GetClientSize().GetWidth() / Board.BoardWidth
		
	def squareHeight(self):	
        ### 블럭의 높이 선언
		return self.GetClientSize().GetHeight() / Board.BoardHeight
		
if __name__ == "__main__":
    #app = wx.PySimpleApp()
    #frame = MyForm()
    #frame.Show()
    #app.MainLoop()


	app = wx.App()
	Tetris(None, title='Tetris')
	app.MainLoop()