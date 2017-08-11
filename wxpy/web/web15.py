#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class CustomLine(wx.Panel): #PyControl
    """
    A custom class for a line
    Modified from http://wiki.wxpython.org/CreatingCustomControls
    """
    def __init__(self, parent, id=wx.ID_ANY, label="", pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.NO_BORDER, validator=wx.DefaultValidator,
            name="CustomLine"):
        """
        Default class constructor.

        @param parent: Parent window. Must not be None.
        @param id: CustomLine identifier. A value of -1 indicates a default value.
        @param label: Text to be displayed next to the checkbox.
        @param pos: CustomLine position. If the position (-1, -1) is specified
                    then a default position is chosen.
        @param size: CustomLine size. If the default size (-1, -1) is specified
                     then a default size is chosen.
        @param style: not used in this demo, CustomLine has only 2 state
        @param validator: Window validator.
        @param name: Window name.
        """
        #~ wx.PyControl.__init__(self, parent, id, pos, size, style, validator, name)
        wx.Panel.__init__(self, parent, id, pos, size, style)

        # Bind the events related to our control: first of all, we use a
        # combination of wx.BufferedPaintDC and an empty handler for
        # wx.EVT_ERASE_BACKGROUND (see later) to reduce flicker
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.lpen = wx.Pen('yellow', 2, wx.SOLID)   
        self.imagebkg = wx.EmptyImage( 10, 10 )
        #~ self.imagebkg.SetData((255,255,255))
        #~ self.imagebkg.SetAlphaData((1))

    def OnPaint(self, event):
        """ Handles the wx.EVT_PAINT event for CustomLine. """

        # If you want to reduce flicker, a good starting point is to
        # use wx.BufferedPaintDC.
        pdc = wx.BufferedPaintDC(self)
        dc = wx.GCDC(pdc) 

        # Is is advisable that you don't overcrowd the OnPaint event
        # (or any other event) with a lot of code, so let's do the
        # actual drawing in the Draw() method, passing the newly
        # initialized wx.BufferedPaintDC
        self.Draw(dc)

    def Draw(self, dc):
        """
        Actually performs the drawing operations, for the bitmap and
        for the text, positioning them centered vertically.
        """

        # Get the actual client size of ourselves
        width, height = self.GetClientSize()

        if not width or not height:
            # Nothing to do, we still don't have dimensions!
            return

        # Initialize the wx.BufferedPaintDC, assigning a background
        # colour and a foreground colour (to draw the text)
        #~ backColour = self.GetBackgroundColour()
        #~ backBrush = wx.Brush((1,1,1,150), wx.TRANSPARENT) # backColour
        #~ backBrush = wx.Brush((10,10,1,150)) # backColour
        dc.SetBackground(wx.TRANSPARENT_BRUSH) #() backBrush
        #~ dc.SetBackgroundMode(wx.TRANSPARENT)
        dc.Clear()

        dc.SetPen(self.lpen)
        dc.DrawLine(0, 0, 100, 100)

    def OnEraseBackground(self, event):
        """ Handles the wx.EVT_ERASE_BACKGROUND event for CustomLine. """

        # This is intentionally empty, because we are using the combination
        # of wx.BufferedPaintDC + an empty OnEraseBackground event to
        # reduce flicker
        pass

class MyTestFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyTestFrame, self).__init__(parent, title=title, 
            size=(250, 150))

        # the master panel of the frame - "Add a panel so it looks correct on all platforms"
        self.panel = wx.Panel(self, wx.ID_ANY)
            # self.panel.SetBackgroundColour(wx.Colour(124, 224, 124)) # to confirm the square is the panel

        self.mpanelA = wx.Panel(self.panel, -1, size=(200,50))
        self.mpanelA.SetBackgroundColour((200,100,200))
        self.mpanelB = wx.Panel(self.panel, -1, size=(50,200), pos=(50,30))
        self.mpanelB.SetBackgroundColour(wx.Colour(200,100,100,100))

        self.cline = CustomLine(self.panel, -1, size=(-1,200))

        self.Centre()
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    MyTestFrame(None, 'Test')
    app.MainLoop()