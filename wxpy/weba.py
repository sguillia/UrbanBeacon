import wx
import logging
import sys

class WxLog(logging.Handler):
	def __init__(self, ctrl):
		logging.Handler.__init__(self)
		self.ctrl = ctrl
	def emit(self, record):
		self.ctrl.AppendText(self.format(record)+"\n")

class MainFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="logging test")
		self.level = 1
		log = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		criticalbtn = wx.Button(self, -1 , 'critical')
		errorbtn = wx.Button(self, -1 , 'error')
		warnbtn = wx.Button(self, -1 , 'warn')
		infobtn = wx.Button(self, -1 , 'info')
		debugbtn = wx.Button(self, -1 , 'debug')
		togglebtn = wx.Button(self, -1 , 'toggle level')
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(log, 1, wx.EXPAND)
		sizer.Add(criticalbtn)
		sizer.Add(errorbtn)
		sizer.Add(warnbtn)
		sizer.Add(infobtn)
		sizer.Add(debugbtn)
		sizer.Add(togglebtn)
		self.SetSizer(sizer)

		self.logr = logging.getLogger('')
		self.logr.setLevel(logging.DEBUG)
		hdlr = WxLog(log)
		hdlr.setFormatter(logging.Formatter('%(levelname)s | %(name)s |%(message)s [@ %(asctime)s in %(filename)s:%(lineno)d]'))
		self.logr.addHandler(hdlr)
		self.logr.debug(str(sys.stdout))

		self.Bind(wx.EVT_BUTTON, self.on_toggle, togglebtn)
		self.Bind(wx.EVT_BUTTON, self.on_critical, criticalbtn)
		self.Bind(wx.EVT_BUTTON, self.on_error, errorbtn)
		self.Bind(wx.EVT_BUTTON, self.on_warn, warnbtn)
		self.Bind(wx.EVT_BUTTON, self.on_info, infobtn)
		self.Bind(wx.EVT_BUTTON, self.on_debug, debugbtn)

	def on_toggle(self, evt):
		self.level = (self.level+1) % 5
		levels = [logging.CRITICAL, logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
		self.logr.setLevel(levels[self.level])
		print self.level, levels[self.level]

	def on_critical(self, evt):
		#self.logr.critical('Test message.')
		print "lol"

	def on_error(self, evt):
		self.logr.error('Test message.')

	def on_warn(self, evt):
		self.logr.warn('Test message.')

	def on_info(self, evt):
		self.logr.info('Test message.')

	def on_debug(self, evt):
		self.logr.debug('Test message.')

if __name__ =="__main__":
	app = wx.App(0)
	frame = MainFrame()
	frame.Show()
	app.MainLoop()
