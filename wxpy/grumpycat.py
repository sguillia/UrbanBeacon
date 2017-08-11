import wx
from utils import *

class grumpyFrame(wx.Dialog):
	"""Unimplemented features"""
	def __init__(self):
		wx.Dialog.__init__(self, parent=None, size=(400, 400+23))
		panel = wx.Panel(self)
		bmp = wx.Image("img/grumpy.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		bmp = scale_bitmap(bmp, 400, 400)
		wx.StaticBitmap(self, -1, bmp, (0, 0), (bmp.GetWidth(), bmp.GetHeight()))
	###
###
