import wx
import sys
import re
import string
import wx.lib.buttons as buttons
from grumpycat import *
from editor import *
from utils import *
from map_panel import *

default_addr = "https://www.google.fr/maps/@48.8965903,2.3183433,9z"

########################################################################
class TabPanel_dump(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""

		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		'''
		#txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
		#txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
		btn_cache = wx.Button(self, label="Read input")
		btn_check = wx.Button(self, label="Check (>)")

		log_send = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.HSCROLL)
		log_uart = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		log_std = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		hSizer.Add(btn_cache, 0, wx.ALL)
		hSizer.Add(btn_check, 0, wx.ALL)
		vSizer = wx.BoxSizer(wx.VERTICAL)
		vSizer.Add(hSizer, 0, wx.TOP)
		vSizer.AddSpacer(5)
		vSizer.Add(log_send, 1, wx.EXPAND)
		vSizer.AddSpacer(5)
		vSizer.Add(log_uart, 1, wx.EXPAND)
		vSizer.AddSpacer(5)
		vSizer.Add(log_std, 1, wx.EXPAND)

		btn_cache.Bind(wx.EVT_BUTTON, self.btn_cache_event)
		btn_check.Bind(wx.EVT_BUTTON, self.btn_check_event)

		self.SetSizer(vSizer)
		###
	###
	def btn_cache_event(self, event):
		pass
	###
	def btn_check_event(self, event):
		pass
	###'''
###

########################################################################
class TabPanel_com(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""

		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

		self.parent = parent

		#txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
		#txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
		btn_cache = wx.Button(self, label="Unused")
		btn_check = wx.Button(self, label="Check '>'")
		self.btn_rx = wx.ToggleButton(self, label="Enable RX")
		btn_gps_enable = wx.Button(self, label="Enable GPS '('")
		btn_gps_disable = wx.Button(self, label="Disable GPS ')'")

		txt_send = wx.StaticText(self, label="Send to Urban device")
		txt_uart = wx.StaticText(self, label="Received from Urban device")
		txt_std = wx.StaticText(self, label="Developer logs")

		self.log_send = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
		self.log_uart = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY)
		log_std = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY)

		redir = RedirectText(log_std)
		sys.stdout = redir

		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		hSizer.Add(btn_cache, 0, wx.ALL)
		hSizer.Add(btn_check, 0, wx.ALL)
		hSizer.Add(self.btn_rx, 0, wx.ALL)
		hSizer.Add(btn_gps_enable, 0, wx.ALL)
		hSizer.Add(btn_gps_disable, 0, wx.ALL)
		vSizer = wx.BoxSizer(wx.VERTICAL)
		vSizer.Add(hSizer, 0, wx.TOP)
		vSizer.AddSpacer(5)
		vSizer.Add(txt_send, 0)
		vSizer.AddSpacer(5)
		vSizer.Add(self.log_send, 0, wx.EXPAND)
		vSizer.AddSpacer(5)
		vSizer.Add(txt_uart, 0)
		vSizer.AddSpacer(5)
		vSizer.Add(self.log_uart, 1, wx.EXPAND)
		vSizer.AddSpacer(5)
		vSizer.Add(txt_std, 0)
		vSizer.AddSpacer(5)
		vSizer.Add(log_std, 1, wx.EXPAND)

		self.log_send.Bind(wx.EVT_TEXT_ENTER, self.send_event)

		btn_cache.Bind(wx.EVT_BUTTON, self.btn_cache_event)
		btn_check.Bind(wx.EVT_BUTTON, self.btn_check_event)
		self.btn_rx.Bind(wx.EVT_TOGGLEBUTTON, self.btn_rx_event)
		btn_gps_enable.Bind(wx.EVT_BUTTON, self.btn_gps_enable_event)
		btn_gps_disable.Bind(wx.EVT_BUTTON, self.btn_gps_disable_event)

		self.SetSizer(vSizer)

		self.delay = 100
		wx.CallLater(self.delay, self.check_input)

		###
	###
	def btn_cache_event(self, event):
		pass
	###
	def send_event(self, event):
		if self.parent.parent.com.com.isOpen():
			packet = self.log_send.GetValue()
			packet = str(packet) # Unicode strings are not supported
			self.parent.parent.com.Write_packet(packet, False, False)
			self.log_send.SetValue("")
		else:
			print "Serial is not open"
	###
	def btn_check_event(self, event):
		if self.parent.parent.com.com.isOpen():
			#print "Serial open"
			self.parent.parent.com.Write_packet(">", False, False)
		else:
			print "Serial is not open"
	###
	def btn_rx_event(self, event):
		if self.btn_rx.GetValue():
			#self.btn_rx.SetLabel("Disable RX")
			self.parent.parent.btn_download.Disable()
			self.parent.parent.btn_upload.Disable()
		else:
			#self.btn_rx.SetLabel("Enable RX")
			self.parent.parent.btn_download.Enable()
			self.parent.parent.btn_upload.Enable()
	###
	def btn_gps_enable_event(self, event):
		self.parent.parent.com.Write_packet("(", 0, 0)
	###
	def btn_gps_disable_event(self, event):
		self.parent.parent.com.Write_packet(")", 0, 0)
	###
	def check_input(self):
		wx.CallLater(self.delay, self.check_input)
		#print "Exec1"
		if not self.btn_rx.GetValue():
			return
		if not self.parent.parent.com.com.isOpen():
			return
		if self.parent.parent.com.active:
			return
		#print "Exec2"
		#num = 
		#if num is 0:
		#	pass # print "No data"
		#else:
		while self.parent.parent.com.com.in_waiting:
			num = self.parent.parent.com.com.in_waiting
			data = self.parent.parent.com.com.read(num)
			string = ''.join([i if ord(i) < 128 else '.' for i in data])
			#print "Num"
			#print num
			#print "Data"
			#print string
			self.log_uart.WriteText(string)
	###
###

class RedirectText:
	def __init__(self,aWxTextCtrl):
		self.out=aWxTextCtrl
	def write(self,string):
		self.out.WriteText(string)

########################################################################
class TabPanel_map(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		self.parent = parent

		btn_showAll = wx.Button(self, label="Show all")
		btn_clear = wx.Button(self, label="Clear")
		btn_newPoint = wx.Button(self, label="New point")
		self.btn_emulator = wx.ToggleButton(self, label="Emulator")
		#btn_emulator_x = wx.Button(self, label="Emulate each")
		self.btn_link = wx.Button(self, label="Get link")
		self.isLink = False

		self.txt1 = wx.TextCtrl(self, style=wx.TE_READONLY|wx.BORDER_NONE)
		self.txt1.SetBackgroundColour(wx.RED)
		font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
		self.txt1.SetFont(font)
		self.txt1.SetBackgroundColour((222, 222, 222, 232))
		#self.txt1.SetValue("N 51' 23.8962\", E 21' 8.067\" - Loading map...")
		self.txt1.SetValue("Loading map...")
		#txt1 = wx.StaticText(self, label="")

		self.urlCheckerRunning = False
		self.mapFullyLoaded = False
		self.gpsmap = MyBrowser(self)
		# Default URL is loaded when first going to map tab
		self.delay = 125
		self.last_url = default_addr
		self.onload_label = None

		self.emulator_set = False	# Emulator timer has been set
		self.emulator = False		# Emulator is running
		
		ctlBox = wx.BoxSizer(wx.HORIZONTAL)
		sp = 1
		self.ctl_buttons = (btn_showAll, btn_clear,
				btn_newPoint, self.btn_emulator, self.btn_link)
		for button in self.ctl_buttons:
			button.Disable()
			ctlBox.Add(button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)

		'''ctlBox.Add(btn_showAll, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)
		ctlBox.Add(btn_clear, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)
		ctlBox.Add(btn_newPoint, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)
		ctlBox.Add(btn_emulator, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)
		ctlBox.Add(btn_emulator_x, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)
		ctlBox.Add(self.btn_link, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=sp)'''
		
		fullBox = wx.BoxSizer(wx.VERTICAL)
		fullBox.Add(ctlBox, proportion=0, flag=wx.EXPAND|wx.TOP, border=0)
		fullBox.AddSpacer(5, 0, 0)
		fullBox.Add(self.txt1, proportion=0, flag=wx.EXPAND, border=0)
		fullBox.AddSpacer(5, 0, 0)
		fullBox.Add(self.gpsmap, proportion=1, flag=wx.EXPAND, border=0)

		self.SetSizer(fullBox)

		btn_showAll.Bind		(wx.EVT_BUTTON, self.btn_showAll_event)
		btn_newPoint.Bind		(wx.EVT_BUTTON, self.btn_newPoint_event)
		btn_clear.Bind			(wx.EVT_BUTTON, self.btn_clear_event)
		self.btn_emulator.Bind	(wx.EVT_TOGGLEBUTTON, self.btn_emulator_event)
		self.btn_link.Bind		(wx.EVT_BUTTON, self.btn_link_event)

		###
	###
	def check_url(self):
		self.urlCheckerRunning = True
		wx.CallLater(self.delay, self.check_url)
		if self.mapFullyLoaded == False:
			return
		new_url = self.gpsmap.browser.GetCurrentURL()
		if new_url != self.last_url:
			self.last_url = new_url
			#print new_url
			#self.txt1.SetValue(new_url)
			self.update_txt(new_url)
			if self.btn_emulator.GetValue():#---------------------------------------------------------------
				self.emulate()
	###
	def emulate(self):
		#self.parent.parent.com.active = True
		# $GPGGA,134205.000,4853.8025,N,00219.1076,E,1,5,1.92,39.5,M,47.3,M,,*62
		url = self.gpsmap.browser.GetCurrentURL()
		r = re.compile('@(.*?)z')
		m = r.search(url)
		if not m:
			self.parent.parent.Warning("Unexpected error",
				"Failed to retrieve GPS coordinates from map url for emulator")
		else:
			data = string.split(m.group(1), ',')
			#print data
			gps_lat = float(data[0])
			gps_lon = float(data[1])
			positive_lat = True if gps_lat > 0 else False
			positive_lon = True if gps_lon > 0 else False
			gps_lat = gps_lat if positive_lat else -gps_lat
			gps_lon = gps_lon if positive_lon else -gps_lon
			gps_coord = (gps_lat, gps_lon)
			nmea_coord = gps2nmea_str(gps_coord)
			coord_NS = 'N' if positive_lat else 'S'
			coord_EW = 'E' if positive_lon else 'W'
			# Sending GPS disable opcode ')'
			# Sending GPS emulaiton opcode '#' (ending by '#')
			gpgga = ")#$GPGGA,134205.000,"+nmea_coord[0]+","+coord_NS+"," \
				+nmea_coord[1]+","+coord_EW+",1,5,1.92,39.5,M,47.3,M,,*62#"
			print "Emulating"
			print str(nmea_coord) + str((coord_NS, coord_EW))
			print "GPGGA sentence :"
			print gpgga
			print "Sending..."
			#
			self.parent.parent.com.Write_packet(gpgga, False)
			#
			#print "Reading response..."
			#rep = self.parent.parent.com.com.readline()
			#if rep:
			#	print "Got response : " + rep
			#else:
			#	print "Failed to get answer !"
			#print self.parent.parent.com.com.readline()[:-1]
			#print self.parent.parent.com.com.readline()[:-1]
			#print self.parent.parent.com.com.readline()[:-1]
			#print self.parent.parent.com.com.readline()[:-1]
			print "Done\n"
			#newPoint = ['1', 'New point', data[0], data[1], data[2]]
			#self.parent.parent.waypoints.append(newPoint)
			#self.parent.tabList.refresh_waypoints()
		#self.parent.parent.com.active = False
	
	###
	def update_txt(self, addr):
		if self.isLink:
			self.txt1.SetValue(addr)
		else:
			self.txt1.SetValue("DD of " + addr)
	###
	def map_loaded(self):
		if self.onload_label is None:
			self.txt1.SetValue("Map loaded !")
		else:
			self.txt1.SetValue(self.onload_label)
		self.mapFullyLoaded = True
		if self.urlCheckerRunning == False:
			wx.CallLater(self.delay, self.check_url)
		for button in self.ctl_buttons:
			button.Enable()
		self.btn_emulator.SetValue(False)
		if not self.parent.parent.btn_connect.connected:
			self.btn_emulator.Disable()
	###
	def btn_showAll_event(self, event):
		if len(self.parent.parent.waypoints) is 0:
			self.txt1.SetValue("There are no waypoints !")
			return
		url = "https://www.google.fr/maps/dir/"
		# wp means waypoints
		for wp in self.parent.parent.waypoints:
			if wp[0] == '0':
				continue
			url = url + wp[2] + "," + wp[3] + "/"
		first = self.parent.parent.waypoints[0]
		url = url + "@" + first[2] + "," + first[3] # + zoom level
		print url
		self.ChangeLocation("All points", "Loading all points...", url)
	###
	def btn_clear_event(self, event):
		self.ChangeLocation(None, "Clearing...", default_addr)
	###
	
	def btn_newPoint_event(self, event):
		url = self.gpsmap.browser.GetCurrentURL()
		r = re.compile('@(.*?)z')
		m = r.search(url)
		if not m:
			self.parent.parent.Warning("Unexpected error",
				"Failed to retrieve GPS coordinates from map url")
		else:
			data = string.split(m.group(1), ',')
			print data
			newPoint = ['1', 'New point', data[0], data[1], data[2]]
			self.parent.parent.waypoints.append(newPoint)
			self.parent.tabList.refresh_waypoints()
	###
	def btn_emulator_event(self, event):
		if self.btn_emulator.GetValue():
			self.txt1.SetValue("New position is sent each time the coordinates do change. \
Release mouse if it doesn't")
			self.parent.parent.com.Write(")")
	###
	'''def enable_emulator(self):
		#if self.emulator_set is False:
		#	wx.CallLater(self.delay, self.emulator_loop)
		#	self.emulator_set = True
		#self.emulator = True'''
	###
	###
	'''def emulator_loop(self):
		print "Emulator loop"
		if self.emulator is True:
			print "Emulator running"
		else:
			print "Emulator not running"
		wx.CallLater(self.delay, self.emulator_loop)'''
	###
	def btn_link_event(self, event):
		if self.isLink is True:
			self.isLink = False
			self.btn_link.SetLabel("Get link")
		else:
			self.isLink = True
			self.btn_link.SetLabel("Get DD")
		addr = self.gpsmap.browser.GetCurrentURL()
		self.update_txt(addr)
	###
	def ChangeLocation(self, new_label, wait_label, new_addr):
		self.txt1.SetValue(wait_label)
		for button in self.ctl_buttons:
			button.Disable()
		self.mapFullyLoaded = False
		self.last_url = new_addr
		self.onload_label = new_label
		self.gpsmap.browser.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.gpsmap.evt_loaded)
		self.gpsmap.browser.loaded = False
		self.gpsmap.browser.LoadURL(new_addr)
	###
###

########################################################################

#https://www.google.fr/maps/@48.8318297,2.2871331,22z -- pt. de versailles
#https://www.google.fr/maps/@48.8834962,2.3273686,22z -- pl. de clichy
#('1', '1', 'Pte de Versailles', '4853.8025', '00219.1076', '35.0'),
#waypoints = [
#		('1', '1', 'Pte de Versailles', '48.8318297', '2.2871331', '35.0'),
#		('2', '1', 'Place de Clichy', '48.8834962', '2.3273686', '35.0')]

class TabPanel_list(wx.Panel):
	def __init__(self, parent, **kwargs):
		""""""
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		self.parent = parent
		#txtOne = wx.TextCtrl(self, wx.ID_ANY, "iiiiiiiii", pos=(200, 200), size=(-1, 50))
		nbPoints = wx.StaticText(self, -1, "X waypoints", style=wx.ALIGN_CENTER)
		#btn_new = wx.Button(self, label="New", size=(10, -1))
		#btn_new = wx.BitmapButton(self, bitmap=wx.Bitmap('img/new.ico'))
		self.btn_new = new_hybrid_button(self, "img/new.ico", "New", 16, 16, 67, 15)
		self.btn_edit = new_hybrid_button(self, "img/edit.ico", "Edit", 16, 16, 67, 15)
		self.btn_del = new_hybrid_button(self, "img/del.ico", "Delete", 16, 16, 67, 15)
		self.btn_edit.Disable()
		self.btn_del.Disable()
		
		distance = wx.StaticText(self, -1, "Total distance X", style=wx.ALIGN_CENTER)
		listBox = wx.BoxSizer(wx.VERTICAL)
		self.list = wx.ListCtrl(self, -1, style = wx.LC_REPORT)
		#self.list = wx.ListCtrl(self, -1, style = wx.LC_EDIT_LABELS)
		self.list.InsertColumn(0, 'Active', width=60, format=wx.LIST_FORMAT_CENTER)
		self.list.InsertColumn(1, 'Label', width=150)
		self.list.InsertColumn(2, 'Latitude', wx.LIST_FORMAT_RIGHT)
		self.list.InsertColumn(3, 'Longitude', wx.LIST_FORMAT_RIGHT)
		self.list.InsertColumn(4, 'Altitude', wx.LIST_FORMAT_RIGHT)

		'''for i in self.waypoints:
			index = self.list.InsertStringItem(sys.maxint, i[0])
			self.list.SetStringItem(index, 1, i[1])
			self.list.SetStringItem(index, 2, i[2])
			self.list.SetStringItem(index, 3, i[3])
			self.list.SetStringItem(index, 4, i[4])
			self.list.SetStringItem(index, 5, i[5])'''
		self.load_waypoints()

		btnBox = wx.BoxSizer(wx.HORIZONTAL)
		btnBox.Add(self.btn_new, proportion=0, border=0, flag=wx.FIXED_MINSIZE)
		btnBox.Add(self.btn_edit, proportion=0, border=0, flag=wx.FIXED_MINSIZE)
		btnBox.Add(self.btn_del, proportion=0, border=0, flag=wx.FIXED_MINSIZE)
		######
		ctlBox = wx.BoxSizer(wx.HORIZONTAL)
		ctlBox.Add(nbPoints, proportion=1, border=5, flag=wx.EXPAND|wx.TOP)
		ctlBox.Add(btnBox, proportion=1, border=0, flag=wx.EXPAND)
		ctlBox.Add(distance, proportion=1, border=5, flag=wx.EXPAND|wx.TOP)
		#distance.SetBackgroundColour(wx.Colour(255,100,100))
		listBox.Add(ctlBox, proportion=0, border=0, flag=wx.EXPAND)
		listBox.AddSpacer(7, 0, 0)
		listBox.Add(self.list, proportion=1, border=0, flag=wx.EXPAND)
		self.SetSizer(listBox)
		parent.Fit()
		self.Centre()
		self.Show(True)
		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.item_activated, self.list)
		
		self.btn_del.Bind(wx.EVT_BUTTON, self.btn_del_event)
		
		self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.item_selected_evt)
		self.list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.item_selected_evt)

		#print "Main frame blocked by dialog"
		#self.item_activated(None)
	######
	'''def item_activated_open_dialog(self, event):
		print "Item activated"
		self.myList = {'valid': 0, 'txt': ''}
		frame = editorFrame(passback=self, passforward=None)
		frame.ShowModal()
		frame.Destroy()
		print self.myList'''
	###
	def item_activated(self, event):
		self.parent.browser_igniter = False
		id = event.m_itemIndex
		lat = self.parent.parent.waypoints[id][2]
		lon = self.parent.parent.waypoints[id][3]
		new_addr = "https://www.google.fr/maps/@"+lat+","+lon+",15z"
		print new_addr
		new_label = self.parent.parent.waypoints[id][1]
		self.parent.tabMap.ChangeLocation(new_label, "Loading waypoint...", new_addr)
		self.parent.parent.notebook.SetSelection(3)
	###
	def btn_del_event(self, event):
		count = self.list.GetSelectedItemCount()
		#if count > 1:
		#response = True
		response = self.parent.parent.Confirm("Confirmation",
				"Are you sure you want to delete " + str(count) + " waypoint" \
				+ ('s' if count > 1 else '') + ' ?')
		if response:
			indexes = []
			i = 0
			next = self.list.GetFirstSelected()
			while next != -1:
				indexes.append(next)
				next = self.list.GetNextSelected(indexes[i])
				i = i + 1
			for listIndex in reversed(indexes):
				del self.parent.parent.waypoints[listIndex]
			self.refresh_waypoints()
	###
	def item_selected_evt(self, event):
		count = self.list.GetSelectedItemCount()
		if count == 0:
			self.btn_edit.Disable()
			self.btn_del.Disable()
		else:
			self.btn_edit.Enable()
			self.btn_del.Enable()
	###
	def load_waypoints(self):
		for i in self.parent.parent.waypoints:
			index = self.list.InsertStringItem(sys.maxint, i[0])
			self.list.SetStringItem(index, 1, i[1])
			self.list.SetStringItem(index, 2, i[2])
			self.list.SetStringItem(index, 3, i[3])
			self.list.SetStringItem(index, 4, i[4])
	###
	def remove_waypoints(self):
		self.list.DeleteAllItems()
	###
	def refresh_waypoints(self):
		self.remove_waypoints()
		self.load_waypoints()
	###
	###
	'''
	def new_hybrid_button(self, path, label, bmp_w, bmp_h, btn_w, btn_h):
		bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
		bmp = scale_bitmap(bmp, bmp_w, bmp_h)
		btn = wx.Button(self, label=label, size=(btn_w, btn_h))
		btn.SetBitmap(bmp)
		return btn
	'''
	###


########################################################################
'''class TabPanel_listx(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""

		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

		sizer = wx.BoxSizer(wx.VERTICAL)
		txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
		sizer.Add(txtOne, 0, wx.ALL, 5)

		self.SetSizer(sizer)
'''

########################################################################
class NotebookDemo(wx.Notebook):
	"""
	Notebook class
	"""

	#----------------------------------------------------------------------
	def __init__(self, parent):
		wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
				wx.BK_DEFAULT
				#wx.BK_TOP
				#x.BK_BOTTOM
				#wx.BK_LEFT
				#wx.BK_RIGHT
				#,
				#size=kwargs['size'], pos=kwargs['pos']
				)
		self.parent = parent
		
		# Avoid browser loading when map tab is selected for the first time,
		#	not by user, but selected by an ListCtrl item activation
		self.browser_igniter = True
		
		self.tabList = TabPanel_list(self)
		self.tabDump = TabPanel_dump(self)
		self.tabCom = TabPanel_com(self)
		self.tabMap = TabPanel_map(self)

		self.AddPage(self.tabList, "List")
		self.AddPage(self.tabDump, "Dump")
		self.AddPage(self.tabCom, "Com")
		self.AddPage(self.tabMap, "Map")
		
		#tabOne.SetBackgroundColour("Gray")

		#self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
		self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

	'''def OnPageChanged(self, event):
		old = event.GetOldSelection()
		new = event.GetSelection()
		sel = self.GetSelection()
		print 'OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel)
		event.Skip()'''

	# Map is not laoded at startup, but when loading map tab
	# Otherwise, the map takes the focus on other fields that are on other tabs
	# Map is loaded once, then event will not be called again
	def OnPageChanging(self, event):
		#old = event.GetOldSelection()
		tab = event.GetSelection()
		if tab is 3 and self.browser_igniter is True:
			self.Unbind(wx.EVT_NOTEBOOK_PAGE_CHANGING)
			self.tabMap.gpsmap.browser.LoadURL(default_addr)
		#sel = self.GetSelection()
		#print 'OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel)
		#event.Skip()


