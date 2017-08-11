#import images
#from PIL import Image as images

import wx
import time
import glob
from notebook import *
from grumpycat import *
from urban import *
import utils

class MyFrame(wx.Frame):
	def __init__(self, parent, ID, title):
		"""Constructor"""
		frame_w = 600
		frame_h = 700
		wx.Frame.__init__(self, parent=None, title=title, pos=(-1, -1),
				size=(frame_w, frame_h), style=wx.DEFAULT_FRAME_STYLE)
		#size=(frame_w, frame_h), style = wx.TRANSPARENT_WINDOW)
		panel = wx.Panel(self, size=(frame_w, frame_h))
		''''if panel.CanSetTransparent:
			panel.SetTransparent(100)
			print "y"
		else:
			print "no"'''

		self.com = UrbanSerial(self)

		#https://www.google.fr/maps/@48.8318297,2.2871331,22z -- pt. de versailles
		#https://www.google.fr/maps/@48.8834962,2.3273686,22z -- pl. de clichy
		#('1', '1', 'Pte de Versailles', '4853.8025', '00219.1076', '35.0'),
		#self.waypoints = [
		#		('1', '1', 'Pte de Versailles', '48.8318297', '2.2871331', '35.0'),
		#		('2', '1', 'Place de Clichy', '48.8834962', '2.3273686', '35.0')]

		self.waypoints = [
				#['1', 'Pte de Versailles', '48.8318297', '2.2871331', '35.0'],
				#['1', 'Place de Clichy', '48.8834962', '2.3273686', '35.0']
				]

		txt1 = wx.StaticText(self, -1, "Serial port : ", size=(-1, -1))
		line = wx.StaticLine(self, size=(100, -1))
		line.SetForegroundColour((255, 0, 0))
		lineBorder1 = wx.StaticText(self, -1, "", size=(10, 5))
		lineBorder2 = wx.StaticText(self, -1, "", size=(10, 1))
		self.notebook = NotebookDemo(self)
		#self.combo1 = wx.ComboBox(self, size=wx.Size(200, -1),
		self.combo1 = wx.ComboBox(self,
				choices=['Choose serial port...'],
				style=wx.CB_READONLY,
				size=(-1, -1))
		self.combo1.update = self.update_combo_list
		self.combo1.update(None)
		self.combo1.SetSelection(0)
		self.btn_connect = wx.Button(self, label="Connect", size=wx.Size(-1, -1))
		self.btn_connect.connected = False
		self.btn_refresh = wx.Button(self, label="Refresh", size=wx.Size(-1, -1))
		self.btn_download = wx.Button(self, label="Download", size=wx.Size(100, -1))
		self.btn_upload = wx.Button(self, label="Upload", size=wx.Size(100, -1))
		self.btn_export = wx.Button(self, label="Export", size=wx.Size(100, -1))
		self.btn_import = wx.Button(self, label="Import", size=wx.Size(100, -1))
		##########
		
		self.btn_connect.Disable()
		self.btn_download.Disable()
		self.btn_upload.Disable()

		##########
		sp = 3
		serialBox = wx.BoxSizer(wx.HORIZONTAL)
		serialBox.Add(txt1, proportion=0, border=4, flag=wx.TOP)
		#serialBox.Add(self.combo1, proportion=0, flag=wx.FIXED_MINSIZE)
		serialBox.Add(self.combo1, proportion=2, flag=wx.EXPAND)
		serialBox.AddSpacer(sp, 0, 0)
		serialBox.Add(self.btn_connect, proportion=1, border=0, flag=wx.EXPAND)
		serialBox.AddSpacer(sp*2, 0, 0)
		serialBox.Add(self.btn_refresh, proportion=1, border=0, flag=wx.EXPAND)
		serialBox.AddSpacer(sp * 2, 0, 0)
		##########
		ioBox = wx.BoxSizer(wx.HORIZONTAL)
		ioBox.AddSpacer(sp, 0, 0)
		ioBox.Add(self.btn_download, proportion=1, flag=wx.LEFT|wx.RIGHT, border=sp)
		ioBox.Add(self.btn_upload, proportion=1, flag=wx.LEFT|wx.RIGHT, border=sp)
		ioBox.Add(self.btn_export, proportion=1, flag=wx.LEFT|wx.RIGHT, border=sp)
		ioBox.Add(self.btn_import, proportion=1, flag=wx.LEFT|wx.RIGHT, border=sp)
		ioBox.AddSpacer(sp, 0, 0)
		##########
		lineBox = wx.BoxSizer(wx.HORIZONTAL)
		lineBox.Add(lineBorder1, proportion=0, flag=wx.EXPAND)
		lineBox.Add(line, 1, wx.FIXED_MINSIZE)
		lineBox.Add(lineBorder2, proportion=0, flag=wx.EXPAND)
		##########
		fullBox = wx.BoxSizer(wx.VERTICAL)
		fullBox.AddSpacer(3, 0, 0)
		fullBox.Add(serialBox, border=sp*2, proportion=0, flag=wx.LEFT|wx.EXPAND)
		fullBox.AddSpacer(3, 0, 0)
		fullBox.Add(lineBox, proportion=0, flag=wx.EXPAND)
		fullBox.Add(ioBox, border=0, proportion=0, flag=wx.EXPAND)
		fullBox.Add(self.notebook, 1, wx.EXPAND)
		self.SetSizer(fullBox)
		###################################
		#self.notebook.ChangeSelection(2)
		'''
		#xtext = wx.TextCtrl(self, style=wx.TE_READONLY|wx.BORDER_NONE, pos=wx.Point(10, 60))
		#xtext.SetValue("Hi hi hi")
		#xtext.SetBackgroundColour(wx.SystemSettings.GetColour(4))
			#self.btn = wx.Button(self, label="Unused", pos=wx.Point(10, 150), size=wx.Size(100, -1))
		#self.bouton = wx.Button(self, label="Trigger", pos=wx.Point(10, 200), size=wx.Size(150, -1))

		#self.addButton = wx.Button(self, label="Add", pos=(0, 0), size=wx.Size(100, 20))
		#self.rmButton = wx.Button(self, label="Rm", pos=(50, 50), size=wx.Size(100, 20))

		'''

		self.Bind(wx.EVT_BUTTON, self.combo1.update, self.btn_refresh)
		self.Bind(wx.EVT_BUTTON, self.connect, self.btn_connect)
		self.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.combo1_change, self.combo1)
		
		self.btn_download.Bind(wx.EVT_BUTTON, self.btn_download_event)
		self.btn_upload.Bind(wx.EVT_BUTTON, self.btn_upload_event)
		#self.btn_export.Bind(wx.EVT_BUTTON, self.grumpy)
		self.btn_export.Bind(wx.EVT_BUTTON, self.btn_export_event)
		self.btn_import.Bind(wx.EVT_BUTTON, self.btn_import_event)

		#self.Bind(wx.EVT_BUTTON, self.creerDiag, self.bouton)

		#txt1.SetFont(wx.Font(18, wx.NORMAL, wx.NORMAL, wx.NORMAL))
	####################
	####################
	def grumpy(self, event):
		frame = grumpyFrame()
		frame.ShowModal()
		frame.Destroy()
	###
	'''def OnKeyUP(self, event):
		# Wait end of transaction before escape
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_ESCAPE:
			self.Close()'''
	###
	def combo1_change(self, event):
		sel = self.combo1.GetSelection()
		if (sel == 0):
			self.btn_connect.Disable()
		else:
			self.btn_connect.Enable()
	###
	def connect(self, event):
		if self.btn_connect.connected:
			self.disconnect()
			self.notebook.tabMap.btn_emulator.Disable()
			self.notebook.tabMap.btn_emulator.SetValue(False)
		else:
			port = self.combo1.Items[self.combo1.GetSelection()]
			if self.com.Connect(port):
				print "Connection to " + port + " succeeded"
				self.combo1.Disable()
				self.btn_refresh.Disable()
				self.btn_download.Enable()
				self.btn_upload.Enable()
				self.btn_connect.SetLabel("Disconnect")
				self.btn_connect.connected = True
				self.notebook.tabMap.btn_emulator.Enable()
			else:
				print "Connection to " + port + " failed"
	###
	def disconnect(self):
		self.combo1.Enable()
		self.btn_refresh.Enable()
		self.btn_download.Disable()
		self.btn_upload.Disable()
		self.btn_connect.SetLabel("Connect")
		self.btn_connect.connected = False
		self.com.Disconnect()
	###
	def update_combo_list(self, event):
		ports = glob.glob('/dev/cu*')
		print "---   --- Listing available serial ports"
		#print 'Ports : %s' % ', '.join(map(str, ports))
		#print ports
		ports.insert(0, 'Choose serial port...')
		sel = self.combo1.GetSelection()
		old = self.combo1.Items[sel] if sel != 0 else ''
		self.combo1.Clear()
		self.combo1.AppendItems(ports)
		if old in ports:
			index = ports.index(old)
		else:
			index = 0
			if hasattr(self, 'btn_connect'):
				self.btn_connect.Disable()
		self.combo1.SetSelection(index)
		###
	###
	###
	def btn_download_event(self, event):
		#raw = utils.pack_list(self.waypoints)
		#self.notebook.tabCom.btn_rx.SetValue(0)
		raw = self.com.Download_eeprom()
		if not raw:
			print "Failed to retrieve eeprom data"
			return		
		print "--- ! --- exported to data1000"		
		utils.write_file("data1000", raw)
		wps = utils.unpack_dump(raw)
		if wps is None:	
			self.Warning("Download failed",
				"Cannot unpack : Wrong format\n" + \
				"Memory can be corrupted")
			return
		self.waypoints = wps
		self.notebook.tabList.refresh_waypoints()
		print "---   --- Done downloading. List refreshed\n"
	###
	def btn_upload_event(self, event):
		#raw = utils.pack_list(self.waypoints)
		utils.flash_eeprom(self.waypoints, self.com)
		#write_file("dump1000", raw)
	###
	def btn_export_event(self, event):
		raw = utils.pack_list(self.waypoints)
		print ""		
		print "--- ! --- Caution : exceptions won't be handled"		
		self.Warning("Unimplemented", "Gonna export to 'export.ub'")
		utils.write_file("export.ub", raw)
		print "Done exporting\n"
	###
	def btn_import_event(self, event):
		#raw = utils.pack_list(self.waypoints)
		self.Warning("Unimplemented",
			"Considering 'import.ub' as source file")
		try:
			f = open("import.ub", "rb")
		except Exception as e:
			self.Warning("Import failed", "Cannot open file : " + str(e))
			return
		raw = f.read(1000)
		check = f.read(1)
		if len(raw) != 1000:
			self.Warning("Import failed", "File is too short")
			return
		if check:
			self.Warning("Import failed", "File is too long")
			return
		wps = utils.unpack_dump(raw)
		if wps is None:	
			self.Warning("Import failed", "Cannot unpack : Wrong format")
			return
		self.waypoints = wps
		self.notebook.tabList.refresh_waypoints()
	###
	###
	def Warning(self, caption, message):
		err = wx.MessageDialog(parent=self, caption=caption,
			message=message, style=wx.OK|wx.CENTRE|wx.ICON_WARNING)
		err.ShowModal()
		err.Destroy()
	###
	def Confirm(self, caption, message):
		err = wx.MessageDialog(parent=self, caption=caption,
			message=message, style=wx.OK|wx.CANCEL|wx.CENTRE|wx.ICON_WARNING)
		response = err.ShowModal()
		err.Destroy()
		return response == wx.ID_OK
	###
###

class TestApp(wx.App):
	def OnInit(self):
		frame = MyFrame(None, -1, "UrbanBeacon")
		self.SetTopWindow(frame)
		frame.Show(True)
		return True

if __name__ == '__main__':
	app = TestApp(0)
	app.MainLoop()

