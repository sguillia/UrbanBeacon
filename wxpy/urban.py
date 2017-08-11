import wx
import serial
import time

class UrbanSerial:
	"""Communication with the UrbanBeacon PCB"""
	def __init__(self, parent):
		self.parent = parent
		self.com = serial.Serial()
		self.com.baudrate = 9600
		self.com.timeout = 4.0
		self.active = False
		###
	###
	def Write(self, data):
		self.active = True
		self.com.write(data)
		self.active = False
	###
	def dump(self):
		print self.com.isOpen()
	###
	def Error(self, message, caption="Serial exception"):
		err = wx.MessageDialog(parent=self.parent, caption=caption,
				message=message, style=wx.OK|wx.CENTRE|wx.ICON_EXCLAMATION)
		err.ShowModal()
		err.Destroy()
	###
	def Connect(self, port):
		if (self.com.isOpen()):
			self.Error("Serial is already open on port " + self.com.port)
		else:
			self.com.port = port
			try:
				self.com.open()
				return True
			except Exception as e:
				self.Error(str(e), "Serial exception from pySerial")
				return False
	###
	def Disconnect(self):
		if (False or self.com.isOpen()):
			try:
				self.com.close()
				print "Closed"
				return True
			except Exception as e:
				self.Error(str(e), "Serial exception from pySerial")
				return False
		else:
			self.Error("Serial is not open !")
			return False
	###
	def Write_packet(self, packet, do_test, verbose=True):
		self.active = True
		if do_test:
			print "        Testing connection"
			self.com.write('>')
			ret = self.com.read()
			print "        Ret is " + str(ret)
		if verbose:
			print "        Flashing..."
		self.com.write(packet)
		if verbose:
			print "        Written"
		if do_test:
			print "        Reading confirm byte"
			print "        " + str(self.com.read())
			print "        Read"
		self.active = False
	###
	def Download_eeprom(self):
		self.active = True
		print "Disabling GPS..."	
		self.com.write(')')
		time.sleep(1)
		print "Clearing input buffer..."
		while self.com.in_waiting:
			in_waiting = self.com.in_waiting
			self.com.read(self.com.in_waiting)
			print "    Cleared " + str(in_waiting) + " bytes"
		print "Downloading..."
		'''try:
			test = self.com.read(1)
			print "Got Test ! This is a bug"
			print "Test is : " + str(test)
		except Exception as e:
			print "Exception"
			print e'''
		self.com.write('*')
		raw = self.com.read(1000)
		confirm = self.com.read(1)
		if not confirm:
			self.Error("No confirmation byte received")
			self.active = False
			return None
		print "Confirmation byte is '"+str(confirm)+"'"
		if str(confirm) != '*':
			self.Error("Confirmation byte is wrong")
			self.active = False
			return None
		self.active = False
		return raw
	###
	###
###
