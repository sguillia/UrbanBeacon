import wx

class TaskBarFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR |
                                              wx.NO_FULL_REPAINT_ON_RESIZE)

        self.tbicon = wx.TaskBarIcon()
        icon = wx.Icon('myicon.ico', wx.BITMAP_TYPE_ICO)
        self.tbicon.SetIcon(icon, '')


app = wx.App(False)
frame = TaskBarFrame(None)
frame.Show(False)
app.MainLoop()