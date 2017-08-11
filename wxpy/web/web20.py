import wx

########################################################################
class SecondFrame(wx.Frame):
	  """"""

	  #----------------------------------------------------------------------
	  def __init__(self):
		   """Constructor"""
		   wx.Frame.__init__(self, None, title="Second Frame")
		   panel = wx.Panel(self)
		   txt = wx.StaticText(panel, label="I'm the second frame!")

 ########################################################################
class Prototype(wx.Frame):

	  #----------------------------------------------------------------------
	  def __init__(self, parent, title):
		   wx.Frame.__init__(self, None, title="First Frame", size=(1240,705))
		   self.UI()
		   self.Centre()
		   self.Show()

	  #----------------------------------------------------------------------
	  def UI(self):
		   self.panel1 = wx.Panel(self, -1)
		   self.sizer = wx.BoxSizer()
		   self.sizer.Add(self.panel1, 1, flag=wx.EXPAND) 
		   b = wx.Button(self.panel1, label='second window', size=(180,100), pos=(650,25))
		   b.Bind(wx.EVT_BUTTON, self.OnB)		

		   self.SetSizer(self.sizer)  

	  #----------------------------------------------------------------------
	  def OnB(self, event):
		   frame = SecondFrame()
		   frame.Show()

 #----------------------------------------------------------------------
app = wx.App(False)
Prototype(None, title='')
app.MainLoop()
