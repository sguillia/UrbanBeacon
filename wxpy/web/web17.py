import wx
import wx.lib.platebtn as platebtn
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Plate Button Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
 
##        btn = platebtn.PlateButton(panel, label="Test", style=platebtn.PB_STYLE_DEFAULT)
        btn = platebtn.PlateButton(panel, label="Gradient", style=platebtn.PB_STYLE_GRADIENT)
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()