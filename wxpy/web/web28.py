import wx 
import wx.html2 

# Paris
#addr = "https://www.google.fr/"
#addr = "https://www.google.fr/maps/@48.8555866,2.3537747,11z" # Paris
#addr="https://www.google.fr/maps/@48.4040743,2.7440894,21z" # green intersection
addr = "https://www.google.fr/maps/@48.8965903,2.3183433,9z" # 42

titles = ('New GPS point', 'GPS Emulator')

class MyBrowser(wx.Dialog):
	def __init__(self, mode):
		wx.Dialog.__init__(self, parent=None, size=(700, 700),
				title="New GPS point (loading...)")
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.btn = wx.Button(self, label="")
		self.btn.Bind(wx.EVT_BUTTON, self.dump)
		self.browser = wx.html2.WebView.New(self)
		self.browser.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.evt_loaded)
		self.browser.loaded = False
		sizer.Add(self.btn, 0, wx.EXPAND, 10) 
		sizer.AddSpacer(10, 0, 0) 
		sizer.Add(self.browser, 1, wx.EXPAND, 10) 
		self.SetSizer(sizer)
		self.browser.LoadURL(addr)
		self.last_url = addr
		self.delay = 500
		wx.CallLater(self.delay, self.check_url)
	def dump(self, event):
		print "Dumping"
		print self.browser.GetCurrentURL()
	def show_crosshair(self, event):
		content = self.browser.GetPageSource()
		common = "position: absolute; \
				background-color: rgba(255, 20, 20, 0.7); \
				user-select: none; \
				-moz-user-select: none; \
				-khtml-user-select: none; \
				-webkit-user-select: none; \
				-o-user-select: none;"
		hline = "<div style='" + common + "\
				z-index: 1; \
				top: calc(50% - 1px); \
				left: 0px; \
				width: 100%; \
				height: 2px; \
				'></div>"
		vline = "<div style='" + common + "\
				z-index: 2; \
				left: calc(50% - 1px); \
				top: 0px; \
				height: 100%; \
				width: 2px; \
				'></div>"
		self.browser.SetPage(hline + vline + content, addr)
	###
	def evt_loaded(self, event):
		if not self.browser.loaded:
			self.browser.loaded = True
			self.show_crosshair(None)
		else:
			self.browser.Unbind(wx.html2.EVT_WEBVIEW_LOADED)
			self.SetTitle("New GPS point")
	def check_url(self):
		new_url = self.browser.GetCurrentURL()
		if new_url != self.last_url:
			self.last_url = new_url
			print new_url
		wx.CallLater(self.delay, self.check_url)
	###
###

if __name__ == '__main__': 
	app = wx.App() 
	dialog = MyBrowser() 
	#dialog.browser.LoadURL("https://www.google.com")
	dialog.Show()
	#dialog.chg(None)
	app.MainLoop()
