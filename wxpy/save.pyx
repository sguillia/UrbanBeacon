#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importation du paquet wxPython
import wx
import time
import glob

# Création d'un nouveau cadre, dérivé du wxPython 'Frame'.
class TestFrame(wx.Frame):
	def __init__(self, parent, ID, title):
		wx.Frame.__init__(self, None, -1, title, pos=(-1, -1), size=(1024, 768))

		panel = wx.Panel(self)

		'''txt1 = wx.StaticText(self, -1, "Serial port : ", wx.Point(10, 10))
		#txt1.SetFont(wx.Font(18, wx.NORMAL, wx.NORMAL, wx.NORMAL))

		xtext = wx.TextCtrl(self, style=wx.TE_READONLY|wx.BORDER_NONE, pos=wx.Point(10, 60))
		xtext.SetValue("Hi hi hi")
		xtext.SetBackgroundColour(wx.SystemSettings.GetColour(4))

		self.combo1 = wx.ComboBox(self, size=wx.Size(200, -1),
				pos=wx.Point(90, 7), choices=['Choose serial port...', 'b', 'c'],
				style=wx.CB_READONLY, value="Choose serial port...")
		self.combo1.update = self.update_combo_list
		self.combo1.SetSelection(0)

		#bouton = wx.Button(panel, -1, "Cliquez-moi!", wx.Point(10, 35), wx.Size(-1, -1))
		self.btn_connect = wx.Button(self, label="Connect", pos=wx.Point(290, 5), size=wx.Size(100, -1))

		self.btn = wx.Button(self, id=-1, label="Serial", pos=wx.Point(10, 150), size=wx.Size(100, -1))
		self.bouton = wx.Button(self, id=-1, label="Cliquez-moi!", pos=wx.Point(10, 200), size=wx.Size(150, -1))

		#self.addButton = wx.Button(self, label="Add", pos=(0, 0), size=wx.Size(100, 20))
		#self.rmButton = wx.Button(self, label="Rm", pos=(50, 50), size=wx.Size(100, 20))

		self.Bind(wx.EVT_BUTTON, self.creerDiag, self.bouton)
		self.Bind(wx.EVT_BUTTON, self.combo1.update, self.btn)

		self.line = wx.StaticLine(self, pos=(10, 40), size=(1004, -1))'''



	# fonction qui affiche une boîte de dialogue
	def creerDiag(self, event):
		dlg = wx.MessageDialog(self, "Merci de m'avoir cliqué, ça fait du bien.",
				"Merci!", wx.ICON_EXCLAMATION | wx.YES_NO | wx.CANCEL)
		dlg.ShowModal()
		dlg.Destroy()
		wx.CallLater(500, self.ft)

	def ft(self):
		print "lol"
		wx.CallLater(500, self.ft)

	def update_combo_list(self, event):
		ports = glob.glob('/dev/ttys0*')
		print ports
		ports.insert(0, 'Choose serial port ...')
		self.combo1.Clear()
		self.combo1.AppendItems(ports)

# Chaque application wxWidgets doit avoir une classe dérivée de wx.App
class TestApp(wx.App):
	def OnInit(self):
		frame = TestFrame(None, -1, "Urban Beacon")
		self.SetTopWindow(frame)
		frame.Show(True)
		return True

if __name__ == '__main__':
	app = TestApp(0) # créer une nouvelle instance de l'application
	app.MainLoop()   # lancer l'application

