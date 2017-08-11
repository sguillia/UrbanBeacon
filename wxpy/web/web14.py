import wx
 
class MyStaticText(wx.Window):
    def __init__(self, parent, label):
        wx.Window.__init__(self, parent, -1)
        self.parent = parent
        self.label = label
        width, height = self.GetTextExtent(label)
        self.SetSize((width, height))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
 
        self.Bind(wx.EVT_PAINT, self.OnPaint)
 
    def OnPaint(self, event):
        x, y = self.GetPositionTuple()
        dc = wx.PaintDC(self)
        l, h = dc.GetTextExtent(self.label)
        self.SetSize((l, h))
        dc = wx.PaintDC(self)
        dc2 = wx.BufferedPaintDC(self.parent)
        dc.Blit(0, 0, l, h, dc2, x, y)
        dc.SetTextBackground(wx.NullColour)
        dc.SetTextForeground(wx.BLACK)
        dc.DrawText(self.label, 0, 0)
 
class MyFrame(wx.Frame):
    def __init__(self ,title=u"MyAPP",fichier=""):
 
        wx.Frame.__init__(self, None,-1,title=title,size=(520,130),style=wx.DEFAULT_FRAME_STYLE)
        self.pan2=wx.Panel(self,-1,size=self.GetClientSize(),style = wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
        self.pan2.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
 
        self.static1=MyStaticText(self.pan2,"Salut 1")
        self.static1.CentreOnParent()
 
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.pan2.Bind(wx.EVT_PAINT,self.OnPaint)
 
    def OnResize(self, event):
        self.pan2.SetSize(self.GetClientSizeTuple())
        self.pan2.Refresh()
        self.static1.CentreOnParent()
 
    def OnPaint(self,evt=None):
        size=self.pan2.GetRect() ## <-- La taille est variable
        dc = wx.BufferedPaintDC(self.pan2)
        dc.GradientFillLinear((0,0,size[2]/2,size[3]),wx.RED,wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU),wx.WEST)
        dc.GradientFillLinear((size[2]/2,0,size[2]/2+1,size[3]),wx.RED,wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU),wx.EAST)
 
class MyApp(wx.App):
    def OnInit(self):
        f = MyFrame()
        f.Show(True)
        self.SetTopWindow(f)
        return True
 
if __name__=='__main__':
    app=MyApp()
    app.MainLoop()