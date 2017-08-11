import wx

class editorFrame(wx.Dialog):
	def __init__(self, **kwargs):
		wx.Dialog.__init__(self, parent=None, size=(400, 500))
		panel = wx.Panel(self)
		pf = kwargs['passforward']
		if pf is not None:
			data = kwargs['passforward']
		else:
			data = ('', '', '', '', '')

		self.txtId = wx.TextCtrl(self, value=data[0])
		self.txtId.Bind(wx.EVT_CHAR, self.validate_digit)
		self.txtActive = wx.TextCtrl(self, value=data[1])
		#self.txtId.SetHint('')
		self.btn_ok = new_hybrid_button()

		fullBox = wx.BoxSizer(wx.VERTICAL)

		kwargs['passback'].myList['valid'] = 1

	def validate_digit(self, event):
		keycode = event.GetKeyCode()
		self.txtId = wx.TextCtrl(self, value=data[0])
		if ch2355r(keycode).isdigit():
			event.Skip()
	###
###
