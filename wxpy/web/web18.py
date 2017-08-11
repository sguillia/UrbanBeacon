import wx
import wx.lib.buttons as buttons
 
class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Button Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
 
        # create a normal toggle button
        button = wx.ToggleButton(panel, label="Press Me")
        button.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
 
        # create a generic toggle button
        gen_toggle_button = buttons.GenToggleButton(panel, -1, "Generic Toggle")
        gen_toggle_button.Bind(wx.EVT_BUTTON, self.onGenericToggle)
 
        # create a normal bitmap button
        bmp = wx.Bitmap("img/new.ico", wx.BITMAP_TYPE_ANY)
        bmapBtn = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp,
                                  size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
 
        # create a generic bitmap button
        genBmapBtn = buttons.GenBitmapButton(panel, bitmap=bmp)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button, 0, wx.ALL, 5)
        sizer.Add(gen_toggle_button, 0, wx.ALL, 5)
        sizer.Add(bmapBtn, 0, wx.ALL, 5)
        sizer.Add(genBmapBtn, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onGenericToggle(self, eventq):
        """"""
        print "Generic toggle button was pressed!"
 
    #----------------------------------------------------------------------
    def onToggle(self, event):
        """
        Print a message when toggled
        """
        print "Button toggled!"
 
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
