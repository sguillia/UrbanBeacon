"""
Overlay a simple grid on a bitmap derived from image file using a PaintDC.

Ray Pasco
pascor(at)verizon(dot)net
2011-04-12-Tue__PM-01-55-16__April

"""

import wx
import wx.html2

addr = "https://google.com/"
addr = "https://www.google.fr/maps/@48.8589996,2.207133,11z/"

#----------------------------------------------------------

class MainFrame( wx.Frame ):

	def __init__( self, parent=None, id=-1, title='wx.PaintDC Test' ):
	
		wx.Frame.__init__( self, parent=parent, id=id, title=title,
						   size=(300, 300), pos=(100, 50) )
		
		frmPanel = wx.Panel( self )
		
		# Read the image file into a bitmap.
		graphicFilename = 'GuidoInTheComfyChair.PNG'
		self.imgBmap = wx.Image( graphicFilename, wx.BITMAP_TYPE_ANY ).ConvertToBitmap()
		bmapSize = self.imgBmap.GetSize()
		bmapSizeX, bmapSizeY = bmapSize
		
		self.imgMargin = 25
		self.imgPanel = wx.Panel( frmPanel, size=bmapSize, pos=(self.imgMargin, self.imgMargin) )
		# Calc and set the Frame interior size so to allow the bitmap to be centered
		#   with a border around it.
		self.ClientSize = (2*self.imgMargin+bmapSizeX, 2*self.imgMargin+bmapSizeY)
		self.imgPanel.browser = wx.html2.WebView.New(self.imgPanel, size=(200, 200))
		self.imgPanel.browser.LoadURL(addr)
		line = wx.StaticLine(self, size=(2*self.imgMargin+bmapSizeX, -1), pos=(0, 150))
		line = wx.StaticLine(self, size=(2*self.imgMargin+bmapSizeX, -1), pos=(0, 251))
		#sizer = wc.BoxSizer(wx.VERTICAL)
		#sizer.Add(self.browser, 1, wx.EXPAND, 10)
		#-----
		
		# Keep track of OnPaint handler calls just for DEBUG info gathering purposes.
		self.paintCtr = 0
		
		wx.EVT_PAINT( self.imgPanel, self.OnPaint )
		
	#end def __init__
	
	#-----
		
	def OnPaint( self, event ):
		
		self.paintCtr += 1;  print '----  OnPaint() ', self.paintCtr
		
		panelDC = wx.PaintDC( self.imgPanel )
		
		# Copy (blit, "Block Level Transfer") a portion of the screen bitmap 
		#   into the returned capture bitmap.
		# The bitmap associated with memDC (captureBmap) is the blit destination.
		#												   # Blit (copy) parameter(s):
		imgPos = (0, 0)
		panelDC.DrawBitmapPoint( self.imgBmap, imgPos )
		
		# Once the BG mode is set to wx.Transparent it cannot be reset to wx.SOLID.
		#panelDC.SetBackgroundMode( wx.TRANSPARENT )	 # wx.SOLID or wx.TRANSPARENT
		panelDC.SetBackgroundMode( wx.SOLID )		   # wx.SOLID or wx.TRANSPARENT
		panelDC.SetTextForeground( wx.WHITE )
		panelDC.SetTextBackground( wx.BLUE )	# has no effect id bg mode is wx.TRANSPARENT
		panelDC.DrawText( ' AB CDEF GHIJ ', 25, 35 )
		
		# Draw a NxM grid pattern - (n+1)+(m+1) lines.
		# Drawing thicker lines would be a bit trickier.
		numRows, numCols = 3, 3
		gridWid, gridHgt = panelDC.GetSizeTuple()
		cellWid = float( gridWid - 1) / numRows
		cellHgt = float( gridHgt - 1) / numCols

		panelDC.SetBrush( wx.Brush( wx.WHITE, wx.TRANSPARENT) )
		panelDC.SetPen( wx.Pen( wx.WHITE, 1, wx.SOLID) )
		panelDC.DrawRectangle( 0, 0, gridWid, gridHgt )

		panelDC.SetPen( wx.Pen( wx.BLUE, 1, wx.SOLID) )
		for rowNum in xrange( numRows + 1) :
			panelDC.DrawLine( 0, rowNum*cellHgt, gridWid, rowNum*cellHgt )

		for colNum in xrange( numCols + 1 ) :
			panelDC.DrawLine( colNum*cellWid, 0, colNum*cellWid, gridHgt )
		
		
		
		event.Skip()	# Very important to let all higher level handlers be called.
		
	#end def OnPaint
	
#end  MainFrame class

#----------------------------------------------------------

if __name__ == '__main__' :
	
	myApp = wx.App( False )   # Send errors to command window, not a pop-up.
	appFrame = MainFrame()
	appFrame.Show()
	myApp.MainLoop()

#end if
