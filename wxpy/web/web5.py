import wx
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="My Form")
 
        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        titleIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        title = wx.StaticText(self.panel, wx.ID_ANY, "My Title")
 
        lblSize = (50, -1)
 
        bmp = wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_OTHER, (16, 16))
        inputOneIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelOne = wx.StaticText(self.panel, wx.ID_ANY, "Name")
        inputTxtOne = wx.TextCtrl(self.panel, wx.ID_ANY,'')
 
        inputTwoIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelTwo = wx.StaticText(self.panel, wx.ID_ANY, "Address")
        inputTxtTwo = wx.TextCtrl(self.panel, wx.ID_ANY,'')
 
        inputThreeIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelThree = wx.StaticText(self.panel, wx.ID_ANY, "Email")
        inputTxtThree = wx.TextCtrl(self.panel, wx.ID_ANY, '')
 
        inputFourIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        labelFour = wx.StaticText(self.panel, wx.ID_ANY, "Phone")
        inputTxtFour = wx.TextCtrl(self.panel, wx.ID_ANY, '')
 
        okBtn = wx.Button(self.panel, wx.ID_ANY, "OK")
        cancelBtn = wx.Button(self.panel, wx.ID_ANY, "Cancel")
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)
 
        topSizer        = wx.BoxSizer(wx.VERTICAL)
        titleSizer      = wx.BoxSizer(wx.HORIZONTAL)
        gridSizer       = wx.GridSizer(rows=4, cols=2, hgap=5, vgap=5)
        inputOneSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer  = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer        = wx.BoxSizer(wx.HORIZONTAL)
 
        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)
 
        # each input sizer will contain 3 items
        # A spacer (proportion=1),
        # A bitmap (proportion=0),
        # and a label (proportion=0)
        inputOneSizer.Add((20,-1), proportion=1)  # this is a spacer
        inputOneSizer.Add(inputOneIco, 0, wx.ALL, 5)
        inputOneSizer.Add(labelOne, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
 
        inputTwoSizer.Add((20,20), 1, wx.EXPAND) # this is a spacer
        inputTwoSizer.Add(inputTwoIco, 0, wx.ALL, 5)
        inputTwoSizer.Add(labelTwo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
 
        inputThreeSizer.Add((20,20), 1, wx.EXPAND) # this is a spacer
        inputThreeSizer.Add(inputThreeIco, 0, wx.ALL, 5)
        inputThreeSizer.Add(labelThree, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
 
        inputFourSizer.Add((20,20), 1, wx.EXPAND) # this is a spacer
        inputFourSizer.Add(inputFourIco, 0, wx.ALL, 5)
        inputFourSizer.Add(labelFour, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
 
        # Add the 3-item sizer to the gridsizer and
        # Right align the labels and icons
        gridSizer.Add(inputOneSizer, 0, wx.ALIGN_RIGHT)
        # Set the TextCtrl to expand on resize
        gridSizer.Add(inputTxtOne, 0, wx.EXPAND)
        gridSizer.Add(inputTwoSizer, 0, wx.ALIGN_RIGHT)
        gridSizer.Add(inputTxtTwo, 0, wx.EXPAND)
        gridSizer.Add(inputThreeSizer, 0, wx.ALIGN_RIGHT)
        gridSizer.Add(inputTxtThree, 0, wx.EXPAND)
        gridSizer.Add(inputFourSizer, 0, wx.ALIGN_RIGHT)
        gridSizer.Add(inputTxtFour, 0, wx.EXPAND)
 
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
 
        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(gridSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)
 
        # SetSizeHints(minW, minH, maxW, maxH)
        self.SetSizeHints(250,300,500,400)
 
        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)
 
 
    def onOK(self, event):
        # Do something
        print "onOK handler"
 
    def onCancel(self, event):
        self.closeProgram()
 
    def closeProgram(self):
        self.Close()
 
 
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
