import wx
import wx.grid as gridlib
 
########################################################################
class MyForm(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Getting the Row/Col")
        panel = wx.Panel(self)
 
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, 8)
        self.myGrid = myGrid
        self.myGrid.GetGridWindow().Bind(wx.EVT_RIGHT_DOWN, self.onRightClick)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onRightClick(self, event):
        """"""
        x, y = self.myGrid.CalcUnscrolledPosition(event.GetX(),
                                                  event.GetY())
        row, col = self.myGrid.XYToCell(x, y)
        print row, col
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()