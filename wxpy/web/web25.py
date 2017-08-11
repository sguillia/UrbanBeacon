import sys
import wx
import wx.lib.newevent

(MyCustomEvent, EVT_CUSTOM) = wx.lib.newevent.NewEvent()

class CustomEventTracker(wx.EvtHandler):
 def __init__(self, log, processingCodeFunctionHandle):
  wx.EvtHandler.__init__(self)
  self.processingCodeFunctionHandle = processingCodeFunctionHandle
  self.log = log
  EVT_CUSTOM(self, self.MyCustomEventHandler)

 def MyCustomEventHandler(self, evt):
  self.log.write(evt.resultOfDialog + '\n')
  self.processingCodeFunctionHandle(evt.resultOfDialog)
  evt.Skip()

class MyPanel2(wx.Panel):
 def __init__(self, parent, log):
  wx.Panel.__init__(self, parent)
  self.log = log

 def OnResults(self, resultData):
  self.log.write("Result data gathered: %s" % resultData)

class MyFrame(wx.Frame):
 def __init__(self, parent, ID = -1, title = "", pos = wx.DefaultPosition,
     size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
  wx.Frame.__init__(self, parent, ID, title, pos, size, style)
  self.panel = panel = wx.Panel(self, -1, style = wx.TAB_TRAVERSAL
       | wx.CLIP_CHILDREN
       | wx.FULL_REPAINT_ON_RESIZE)
  sizer = wx.BoxSizer(wx.VERTICAL)
  sizer.Add((25, 25))

  row = wx.BoxSizer(wx.HORIZONTAL)
  row.Add((25,1))
  m_close = wx.Button(self.panel, wx.ID_CLOSE, "Close")
  m_close.Bind(wx.EVT_BUTTON, self.OnClose)
  row.Add(m_close, 0, wx.ALL, 10)
  sizer.Add(row)
  self.panel.SetSizer(sizer)

 def OnClose(self, evt):
  dlg = wx.MessageDialog(self, 
   "Do you really want to close this frame?",
   "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
  result = dlg.ShowModal()
  dlg.Destroy()
  if result == wx.ID_CANCEL:
   event = MyCustomEvent(resultOfDialog = "User Clicked CANCEL")
   self.GetEventHandler().ProcessEvent(event)
  else: # result == wx.ID_OK
   event = MyCustomEvent(resultOfDialog = "User Clicked OK")
   self.GetEventHandler().ProcessEvent(event)
   self.Destroy()

app = wx.App(False)
f2 = wx.Frame(None, title="Frame 1 (for feedback)", size=(400, 350))
p2 = MyPanel2(f2, sys.stdout)
f2.Show()
eventTrackerHandle = CustomEventTracker(sys.stdout, p2.OnResults)
f1 = MyFrame(None, title="PushEventHandler Tester (deals with on close event)", size=(400, 350))
f1.PushEventHandler(eventTrackerHandle)
f1.Show()
app.MainLoop()