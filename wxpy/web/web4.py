COLORS = ["red", "blue", "black", "yellow", "green"]
NUMBERS = ['0', '1', '2', '3', '4']
PANELS = ["Things", "More things", "Ultra!"]

import random
import wx

class TabPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.SetBackgroundColour(random.choice(COLORS))
        self.listBox = wx.ListBox(self, size=(200, -1), choices=NUMBERS, style=wx.LB_SINGLE)
#        self.button = wx.Button(self, label="Something else here? Maybe!")

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.listBox, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
#        self.sizer.Add(self.button, proportion=1, flag=wx.ALL)

        self.SetSizer(self.sizer)


class MyNotebook(wx.Notebook):
    def __init__(self, *args, **kwargs):
        wx.Notebook.__init__(self, *args, **kwargs)

        self.panels = []
        for name in PANELS:
            panel = TabPanel(self)
            self.panels.append(panel)
            self.AddPage(panel, name)


class MyPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.notebook = MyNotebook(self, size=(400, -1))
#        self.button = wx.Button(self, label="Something else here? Maybe!")

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.notebook, proportion=0, flag=wx.EXPAND)
#        self.sizer.Add(self.button, proportion=0)
        self.SetSizer(self.sizer)


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = MyPanel(self)

        self.status = self.CreateStatusBar()

        self.menubar = wx.MenuBar()
        first=wx.Menu()
        second=wx.Menu()
        first.Append(wx.NewId(), "New", "Creates A new file")
        first.Append(wx.NewId(), "ADID", "Yo")
        self.menubar.Append(first, "File")
        self.menubar.Append(second, "Edit")
        self.SetMenuBar(self.menubar)

        self.Show()


app = wx.App(False)
win = MainWindow(None, size=(600, 400))
app.MainLoop()