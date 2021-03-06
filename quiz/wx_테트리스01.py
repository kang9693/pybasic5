
import wx
import random


class Tetris(wx.Frame):
    
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(180, 380))
        
		self.initFrame()
    
	def initFrame(self):

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText('0')
		
		## board 초기화 
		self.board = Board(self)
		
		self.board.SetFocus()
		self.board.start()

		self.Centre()  ## board 위치 
		self.Show(True)
       

class Board(wx.Panel):
    
	BoardWidth = 10
	BoardHeight = 22
	Speed = 1600
	ID_TIMER = 1
	
	while 
	#threading 
	#

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)        
		self.initBoard()
        
	def initBoard(self):    
	
		

		self.timer = wx.Timer(self, Board.ID_TIMER)
		self.isWaitingAfterLine = False
		self.curPiece = Shape()
		self.nextPiece = Shape()
		self.curX = 0
		self.curY = 0
		self.numLinesRemoved = 0
		self.board = []

		self.isStarted = False
		self.isPaused = False
		
		#while 

		self.Bind(wx.EVT_PAINT, self.OnPaint)				      ### 
		self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)				  ###
		self.Bind(wx.EVT_TIMER, self.OnTimer, id=Board.ID_TIMER)  ### OnTimer ## Grphic 반복

		self.clearBoard()

	def shapeAt(self, x, y):
		#print(x,y,Board.BoardWidth)
		x=int(x)        
		return self.board[(y * Board.BoardWidth) + x]

	def setShapeAt(self, x, y, shape):
		#print(x,y,Board.BoardWidth)	
		x=int(x)
		self.board[(y * Board.BoardWidth) + x] = shape

	def squareWidth(self):
        
		return self.GetClientSize().GetWidth() / Board.BoardWidth

	def squareHeight(self):
        
		return self.GetClientSize().GetHeight() / Board.BoardHeight

	def start(self):   ## 게임 메인 루트 시작
        
		if self.isPaused:
			return

		self.isStarted = True
		self.isWaitingAfterLine = False
		self.numLinesRemoved = 0
		self.clearBoard()

		self.newPiece()
		
		self.timer.Start(Board.Speed)   ### timer 를 이용한 게임 속제 제어 

	def pause(self):    ## 게임 일시정지
        
		if not self.isStarted:
			return

		self.isPaused = not self.isPaused
		statusbar = self.GetParent().statusbar

		if self.isPaused:
			self.timer.Stop()
			statusbar.SetStatusText('paused')
		else:
			self.timer.Start(Board.Speed)
			statusbar.SetStatusText(str(self.numLinesRemoved))

		self.Refresh()

	def clearBoard(self):
        
		for i in range(Board.BoardHeight * Board.BoardWidth):
			self.board.append(Tetrominoes.NoShape)

	def OnPaint(self, event):

		dc = wx.PaintDC(self)        

		size = self.GetClientSize()
		boardTop = size.GetHeight() - Board.BoardHeight * self.squareHeight()
        
		for i in range(Board.BoardHeight):
			for j in range(Board.BoardWidth):
				shape = self.shapeAt(j, Board.BoardHeight - i - 1)
				if shape != Tetrominoes.NoShape:
					self.drawSquare(dc,
						0 + j * self.squareWidth(),
						boardTop + i * self.squareHeight(), shape)

						
		if self.curPiece.shape() != Tetrominoes.NoShape:
			for i in range(4):
				x = self.curX + self.curPiece.x(i)
				y = self.curY - self.curPiece.y(i)
				self.drawSquare(dc, 0 + x * self.squareWidth(),
					boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
						self.curPiece.shape())


	def OnKeyDown(self, event):
        
		if not self.isStarted or self.curPiece.shape() == Tetrominoes.NoShape:
			event.Skip()
			return
		controlDown = event.CmdDown()
		keycode = event.GetKeyCode()
		#print(controlDown)
		
		#print (keycode)
		if keycode == ord('P') or keycode == ord('p'):
			#print ( keycode )
			self.pause()
			return
		self.isPaused=1
		##print("wx.WXK_LEFT:",wx.WXK_LEFT)
		##print(type(wx.WXK_LEFT))
		if not self.isPaused:
			return	
		########################## keyboard 제어 ########################
		#print (keycode)
		#print(wx.WXK_LEFT)
		elif keycode == 328:  # LEFT_Key ( 328 )
			#print (keycode)
			#print("wx.WXK_LEFT")
			#print(self.curPiece, self.curX,self.curY)
			self.tryMove(self.curPiece, self.curX - 1, self.curY)
		
		elif keycode == 330:
			#print (keycode)
			self.tryMove(self.curPiece, self.curX + 1, self.curY)
		
		
		### 블록회전
		elif keycode ==  332: # wx.WXK_DOWN:
			#print (keycode)
			self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)
		
		### 블록회전 
		elif keycode == 326: #wx.WXK_UP:
			#print (keycode)
			self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)
		

		### drop down
		elif keycode == wx.WXK_SPACE:  ## space bar   dropDown 
			#print (keycode)
			self.dropDown()
	

		### 한줄 아래로 내리기
		elif keycode == ord('D') or keycode == ord('d'):
			self.oneLineDown()
		else:
			event.Skip()


	def OnTimer(self, event):
        
		if event.GetId() == Board.ID_TIMER:
			if self.isWaitingAfterLine:
				self.isWaitingAfterLine = False
				self.newPiece()
			else:
				self.oneLineDown()
		else:
			event.Skip()


	def dropDown(self):
        
		newY = self.curY
        
		while newY > 0:
			if not self.tryMove(self.curPiece, self.curX, newY - 1):
				break
			newY -= 1

		self.pieceDropped()

	def oneLineDown(self):
        
		if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
			self.pieceDropped()   ## 한칸아래로 이등 
            

	def pieceDropped(self):
        
		for i in range(4):
			x = self.curX + self.curPiece.x(i)
			y = self.curY - self.curPiece.y(i)
			self.setShapeAt(x, y, self.curPiece.shape())

		self.removeFullLines()

		if not self.isWaitingAfterLine:
			self.newPiece()


	def removeFullLines(self):  ###  한줄씩 없애기
    
		numFullLines = 0

		statusbar = self.GetParent().statusbar

		rowsToRemove = []   ## row line 없애기

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

		
		if not self.tryMove(self.curPiece, self.curX, self.curY):
            
			self.curPiece.setShape(Tetrominoes.NoShape)
			self.timer.Stop()
			self.isStarted = False
			statusbar.SetStatusText('Game over')
            

	def tryMove(self, newPiece, newX, newY):
		#print("testing")
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

		pen = wx.Pen(light[shape])   ## 블록을 그린다.
		pen.SetCap(wx.CAP_PROJECTING)
		dc.SetPen(pen)

		#dc.DrawLine(x, y + self.squareHeight() - 1, x, y)
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
		dc.DrawRectangle(x + 1, y + 1, self.squareWidth() - 2,self.squareHeight() - 2)


class Tetrominoes(object):
    
	NoShape = 0
	ZShape = 1
	SShape = 2
	LineShape = 3
	TShape = 4
	SquareShape = 5
	LShape = 6
	MirroredLShape = 7


class Shape(object):
    
	coordsTable = (
        ((1, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

	def __init__(self):
        
		self.coords = [[0,0] for i in range(4)]
		#self.pieceShape = Tetrominoes.NoShape

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
	### 블록 회전 
	def rotatedLeft(self):
        
		if self.pieceShape == Tetrominoes.SquareShape:
			return self

		result = Shape()
		result.pieceShape = self.pieceShape
        
		for i in range(4):
			result.setX(i, self.y(i))
			result.setY(i, -self.x(i))

		return result
	
	### 블록 회전 
	def rotatedRight(self):
        
		if self.pieceShape == Tetrominoes.SquareShape:
			return self

		result = Shape()
		result.pieceShape = self.pieceShape
        
		for i in range(4):
			result.setX(i, -self.y(i))
			result.setY(i, self.x(i))

		return result

if __name__ == "__main__":
	app = wx.App()     ## 무조건 wx.App()
	Tetris(None, title='Tetris')
	app.MainLoop()   #