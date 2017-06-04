import wx       # wxpython 
import random   # random

# class   상속  
## class  
## class => 함수들의 집함   
##  
## 2:53 : 03:05 
## pyQT          ##    QT 유닉스 계열에서 GUI 관련 개발 py, c, java, 
## pyside        ##     pyside   
## wxpython      ##    wxpython 윈도우 스타일 완전히 windows api 를 가져다 쓸수 있음 윈도우와 비슷하게 구현
## 참고 python GUI 힘들어.. 이유 화면에 프레임을 그려주는 것이 느리고 깜박임이 심함 로딩 느림
## 인터프린터 엔진 

class Tetris(wx.Frame):                 ## class   ## wx.Frame < === 화면 그림 그리는네 
    
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title='tetris', size=(180, 380))
		#메인 프래임 설정
		#wx.Frame.
        
		self.initFrame()   # 메인프레임 초기화
    
	def initFrame(self):

		self.statusbar = self.CreateStatusBar()   ### 상태봐 생성 
		self.statusbar.SetStatusText('0')
		self.board = Board(self)   # 보드 초기화 
		self.board.SetFocus()        
		#self.board.start()

        #self.Centre()
		self.Center()
		self.Show(True)
		
class Board(wx.Panel):    
    
	
	BoardWidth = 10   ## 보드 폭  선언
	BoardHeight = 22  ## 보드 높이 선언
	Speed = 300    		### 속도
	ID_TIMER = 1

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
        
		self.initBoard()
        
	def initBoard(self):    
		#wx.Frame을 초기화 한다. 
		# 여기에서의 초기화 wx.Frame에 대한 초기화를 이야기 한다. 
		self.timer = wx.Timer(self, Board.ID_TIMER)
		self.isWaitingAfterLine = False
		self.curPiece = Shape()
		self.nextPiece = Shape()
		self.curX = 0                   ###
		self.curY = 0                   ###
		self.numLinesRemoved = 0
		self.board = []

		self.isStarted = False
		self.isPaused = False

		self.Bind(wx.EVT_PAINT, self.OnPaint)   
		self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)    ### 키 컨트롤
		self.Bind(wx.EVT_TIMER, self.OnTimer, id=Board.ID_TIMER)

		#self.clearBoard()
		
		
		
		
	def shapeAt(self, x, y):
        
		return self.board[(y * Board.BoardWidth) + x]   ## 보더 폭 사이즈 제어 
		
	
	def setShapeAt(self, x, y, shape):
        
		self.board[(y * Board.BoardWidth) + x] = shape
	
	## 블럭의 크기 제어
	def squareWidth(self):
        
		return self.GetClientSize().GetWidth() / Board.BoardWidth
		
	def squareHeight(self):	
        ### 블럭의 높이 선언
		return self.GetClientSize().GetHeight() / Board.BoardHeight
		
		
		
	def start(self):
        
		if self.isPaused:
			return

		self.isStarted = True
		self.isWaitingAfterLine = False
		self.numLinesRemoved = 0
		self.clearBoard()

		self.newPiece()
		self.timer.Start(Board.Speed)
	

		
	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		size = self.GetClientSize()		
		print("test")
		boardTop = size.GetHeight() - Board.BoardHeight * self.squareHeight()
		
			
	def OnTimer(self, event):
        
		if event.GetId() == Board.ID_TIMER:
			if self.isWaitingAfterLine:
				self.isWaitingAfterLine = False
				self.newPiece()
			else:
				print('oneLineDown')
				self.oneLineDown()
		else:
			event.Skip()
	
	
	def OnKeyDown(self, event):
        
		if not self.isStarted or self.curPiece.shape() == Tetrominoes.NoShape:
			event.Skip()
			return

		keycode = event.GetKeyCode()

		if keycode == ord('P') or keycode == ord('p'):
			self.pause()
			return
		if self.isPaused:
			return
        
		elif keycode == wx.WXK_LEFT:
			self.tryMove(self.curPiece, self.curX - 1, self.curY)
        
		elif keycode == wx.WXK_RIGHT:
			self.tryMove(self.curPiece, self.curX + 1, self.curY)
			
		elif keycode == wx.WXK_DOWN:
			self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)
		elif keycode == wx.WXK_UP:
			self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)
		elif keycode == wx.WXK_SPACE:
			self.dropDown()
		elif keycode == ord('D') or keycode == ord('d'):
			self.oneLineDown()
		else:
			event.Skip()
			
	def newPiece(self):
        
		self.curPiece = self.nextPiece
		statusbar = self.GetParent().statusbar
		self.nextPiece.setRandomShape()
		self.curX = Board.BoardWidth / 2 + 1
		self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

		if not self.tryMove(self.curPiece, self.curX, self.curY):
            
			self.curPiece.setShape(Tetrominoes.NoShape)
			self.timer.Stop()
			self.isStarted = False
			statusbar.SetStatusText('Game over')
			
	def clearBoard(self):
        
		for i in range(Board.BoardHeight * Board.BoardWidth):
			self.board.append(Tetrominoes.NoShape)
			
	def dropDown(self):
        
		newY = self.curY
        
		while newY > 0:
			if not self.tryMove(self.curPiece, self.curX, newY - 1):
				break
			
			newY -= 1

		self.pieceDropped()

	def oneLineDown(self):
        
		if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
			self.pieceDropped()
			
	          

	def pieceDropped(self):
        
		for i in range(4):
			x = self.curX + self.curPiece.x(i)
			y = self.curY - self.curPiece.y(i)
			self.setShapeAt(x, y, self.curPiece.shape())

		self.removeFullLines()
		
		
		if not self.isWaitingAfterLine:
			self.newPiece()
			
	def rotatedLeft(self):
        
		if self.pieceShape == Tetrominoes.SquareShape:
			return self

		result = Shape()
		result.pieceShape = self.pieceShape
        
		for i in range(4):
			result.setX(i, self.y(i))
			result.setY(i, -self.x(i))

		return result

	def removeFullLines(self):
    
		numFullLines = 0

		statusbar = self.GetParent().statusbar

		rowsToRemove = []

		for i in range(Board.BoardHeight):
			n = 0
			for j in range(Board.BoardWidth):
				if not self.shapeAt(j, i) == Tetrominoes.NoShape:
					n = n + 1

			if n == 10:
				rowsToRemove.append(i)

		rowsToRemove.reverse()

		for m in rowsToRemove:
			for k in range(m, Board.BoardHeight):
				for l in range(Board.BoardWidth):
						self.setShapeAt(l, k, self.shapeAt(l, k + 1))

			numFullLines = numFullLines + len(rowsToRemove)

			if numFullLines > 0:
				self.numLinesRemoved = self.numLinesRemoved + numFullLines
				statusbar.SetStatusText(str(self.numLinesRemoved)) 
				self.isWaitingAfterLine = True
				self.curPiece.setShape(Tetrominoes.NoShape)
				self.Refresh()


	def newPiece(self):
        
		self.curPiece = self.nextPiece
		statusbar = self.GetParent().statusbar
		self.nextPiece.setRandomShape()
		self.curX = Board.BoardWidth / 2 + 1
		self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
		print(self.curY)

		if not self.tryMove(self.curPiece, self.curX, self.curY):
            
			self.curPiece.setShape(Tetrominoes.NoShape)
			self.timer.Stop()
			self.isStarted = False
			statusbar.SetStatusText('Game over')
            

	def tryMove(self, newPiece, newX, newY):
        
		for i in range(4):
            
			x = newX + newPiece.x(i)
			y = newY - newPiece.y(i)
            
			if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
				return False
			if self.shapeAt(x, y) != Tetrominoes.NoShape:
				return False

		self.curPiece = newPiece
		self.curX = newX
		self.curY = newY
		self.Refresh()
        
		return True


	def drawSquare(self, dc, x, y, shape):
        
		colors = ['#000000', '#CC6666', '#66CC66', '#6666CC',
                  '#CCCC66', '#CC66CC', '#66CCCC', '#DAAA00']

		light = ['#000000', '#F89FAB', '#79FC79', '#7979FC', 
                 '#FCFC79', '#FC79FC', '#79FCFC', '#FCC600']

		dark = ['#000000', '#803C3B', '#3B803B', '#3B3B80', 
                 '#80803B', '#803B80', '#3B8080', '#806200']

		pen = wx.Pen(light[shape])
		pen.SetCap(wx.CAP_PROJECTING)
		dc.SetPen(pen)

		dc.DrawLine(x, y + self.squareHeight() - 1, x, y)
		dc.DrawLine(x, y, x + self.squareWidth() - 1, y)

		darkpen = wx.Pen(dark[shape])
		darkpen.SetCap(wx.CAP_PROJECTING)
		dc.SetPen(darkpen)

		dc.DrawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
		dc.DrawLine(x + self.squareWidth() - 1, 
		y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

		dc.SetPen(wx.TRANSPARENT_PEN)
		dc.SetBrush(wx.Brush(colors[shape]))
		dc.DrawRectangle(x + 1, y + 1, self.squareWidth() - 2, 
		self.squareHeight() - 2)
			

class Shape(object):
    
	coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
	)

	
	### 블록을 관리한다. 
	def __init__(self):
        
		self.coords = [[0,0] for i in range(4)]
		self.pieceShape = Tetrominoes.NoShape

		self.setShape(Tetrominoes.NoShape)
		
	def shape(self):
        
		return self.pieceShape
	
	def setShape(self, shape):
        
		table = Shape.coordsTable[shape]
		for i in range(4):
			for j in range(2):
				self.coords[i][j] = table[i][j]

		self.pieceShape = shape

	def setRandomShape(self):
        
		self.setShape(random.randint(1, 7))

	def x(self, index):
        
		return self.coords[index][0]

	def y(self, index):
        
		return self.coords[index][1]

	def setX(self, index, x):
        
		self.coords[index][0] = x

	def setY(self, index, y):
        
		self.coords[index][1] = y

	def minX(self):
        
		m = self.coords[0][0]
		for i in range(4):
			m = min(m, self.coords[i][0])

		return m

	def maxX(self):
        
		m = self.coords[0][0]
		for i in range(4):
			m = max(m, self.coords[i][0])

		return m

	def minY(self):
        
		m = self.coords[0][1]
		for i in range(4):
			m = min(m, self.coords[i][1])

		return m

	def maxY(self):
        
		m = self.coords[0][1]
        
		for i in range(4):
			m = max(m, self.coords[i][1])

		return m

	def rotatedLeft(self):
        
		if self.pieceShape == Tetrominoes.SquareShape:
			return self

		result = Shape()
		result.pieceShape = self.pieceShape
        
		for i in range(4):
			result.setX(i, self.y(i))
			result.setY(i, -self.x(i))

		return result

	def rotatedRight(self):
        
		if self.pieceShape == Tetrominoes.SquareShape:
			return self

		result = Shape()
		result.pieceShape = self.pieceShape
        
		for i in range(4):
			result.setX(i, -self.y(i))
			result.setY(i, self.x(i))

		return result
		

  

		
### 기본값들 셋팅		
class Tetrominoes(object):
    
	NoShape = 0
	ZShape = 1
	SShape = 2
	LineShape = 3
	TShape = 4
	SquareShape = 5
	LShape = 6
	MirroredLShape = 7	
#if __main__=="__main__":
app = wx.App()
Tetris(None, title='Tetris')  # 메인클래스 
app.MainLoop()