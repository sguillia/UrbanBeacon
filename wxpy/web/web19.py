import wxversion
import wx

class App(wx.App):
	def OnInit(self):
		frame = window()
		frame.Show()
		self.SetTopWindow(frame)
		return True

class window(wx.Frame):
	title = "Main Menu"
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Window', size = (1000, 700))
		panel = wx.Panel(self, -1)
		
		self.SetBackgroundColour(wx.Colour(100, 100, 100))
		self.Centre()
		self.Show()
		
		status = self.CreateStatusBar()
	
		menubar = wx.MenuBar()
		filemenu = wx.Menu()
		exitmenu = filemenu.Append(wx.NewId(), "Exit", "Exit Program")
		
		menubar.Append(filemenu, "File")
		self.Bind(wx.EVT_MENU, self.onExit, exitmenu)
		self.SetMenuBar(menubar)
		
		font1 = wx.Font(30, wx.MODERN, wx.NORMAL, wx.NORMAL, False, 'Consolas')
		
		Text1 = wx.StaticText(panel, -1, "Rhythm Trainer", (10, 15))
		Text1.SetFont(font1)
		Text1.SetForegroundColour('white')
		self.Show(True)
		
		btn1 = wx.Button(panel, label = 'Basic', pos = (100, 200), size = (150, 50))
		btn1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, 'Consolas'))
	
		btn1.Bind(wx.EVT_BUTTON, self.window2_wrap)
	
		btn2 = wx.Button(panel, label = 'Advanced', pos = (100, 270), size = (150, 50))
		btn2.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, 'Consolas'))
		
		btn3 = wx.Button(panel, label = 'Notations', pos = (100, 340), size = (150, 50))
		btn3.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, 'Consolas'))
		
		btn4 = wx.Button(panel, label = 'Settings', pos = (100, 410), size = (150, 50))
		btn4.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, 'Consolas'))
		
		btn5 = wx.Button(panel, label = "Quit", pos = (820, 550), size = (150, 50))
		btn5.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, 'Consolas'))
		self.Bind(wx.EVT_BUTTON, self.OnClick, btn5)

	def OnClick(self, event):
		self.Close()
	
	def OnQuitButton(self, event):
		wx.Sleep(1)
		self.Destroy()
	
	def onExit(self, event):
		self.Destroy()
	
	def newwindow(self, event):
		window2.show

	def window2_wrap(self, event):
		myWin = window2(self)

class window2(wx.Frame):
	title = "new Window"

	def __init__(self, parent, id):
		wx.Frame.__init__(self, id, 'Window2', size = (1000, 700))
		panel = wx.Panel(self, -1)
		self.SetBackgroundColour(wx.Colour(100, 100, 100))
		self.Centre()
		self.Show()


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = window(None, -1)
	frame.Show()
	app.MainLoop()
