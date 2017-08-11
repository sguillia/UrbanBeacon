import wx
import sys

class MainFrame(wx.App):
	def __init__(self, redirect=False, filename=None):
		wx.App.__init__(self, redirect, filename)

	def OnInit(self):
		self.frame = wx.Frame(None, -1, title='Redirect Test',
		size=(620,450),
		style=wx.STAY_ON_TOP|
		wx.DEFAULT_FRAME_STYLE)
		panel = wx.Panel(self.frame, -1)
		self.log = wx.TextCtrl(panel, -1, size=(500,400),
		style = wx.TE_MULTILINE|wx.TE_READONLY|
		wx.HSCROLL)
		redir=RedirectText(self.log)
		sys.stdout=redir
		print 'test'

		#self.frame.Show()
		return True

class RedirectText:
	def __init__(self,aWxTextCtrl):
		self.out=aWxTextCtrl
	def write(self,string):
		self.out.WriteText(string)

if __name__ =="__main__":
	app = wx.App(0)
	frame = MainFrame()
	frame.Show()
	app.MainLoop()

