import wx

class TransparentAwareFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)
		self.transparency = 255

	def SetTransparent(self, value):
		self.transparency = value
		wx.Frame.SetTransparent(self, value)

	def GetTransparent(self):
		return self.transparency		

class MainWindow(TransparentAwareFrame):
	def __init__(self, *args, **kwargs):
		TransparentAwareFrame.__init__(self, *args, **kwargs)
		self.button = wx.Button(self, label="Click me!")
		self.Show()	
		self.button.Bind(wx.EVT_BUTTON, self.onButton)

	def onButton(self, e):
		print self.GetTransparent()
		#self.SetTransparent(self.GetTransparent() - 0)
		self.SetTransparent(0)

app = wx.App(False)
win = MainWindow(None)
app.MainLoop()
