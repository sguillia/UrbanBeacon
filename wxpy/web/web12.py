import wx

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.GREEN)

        self.list = wx.ListCtrl(self, style=wx.LC_REPORT, size=(200, -1))
        column_size = self.list.GetSize()[0] / 2 - 2
        self.list.InsertColumn(0, 'Name')
        self.list.InsertColumn(1, 'Age')   
        self.list.SetColumnWidth(0, column_size)
        self.list.SetColumnWidth(1, column_size)

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.list, proportion=0, flag=wx.EXPAND)
        self.sizer.Add(self.panel, proportion=1, flag=wx.EXPAND)

        self.SetSizerAndFit(self.sizer)
        self.SetSize((600, 400))       
        self.Show()

app = wx.App(False)
win = MainWindow(None)
app.MainLoop()