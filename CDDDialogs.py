import wx
from resource import *

#----------------------------------------------------------------------        
class SetShaftCountDialog(wx.Dialog):
    """
    """
    #----------------------------------------------------------------------
    def __init__(self, shaft, treadle, shed):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Loom Setup", size=(300,225))
        # print shaft
        curShaft = str(shaft)
        curTreadle = str(treadle)
        curShedType = shed

        self.shaftcount = wx.ComboBox(self, choices=LOOM_SHAFT_COUNT_LIST, value=curShaft, pos=(240, 15),style=wx.CB_READONLY)
        wx.StaticText(self, label='Set number of Shafts:', pos=(15, 20), size=(200, 45))

        self.treadlecount = wx.ComboBox(self, choices=LOOM_TREADLE_COUNT_LIST, value=curTreadle, pos=(240, 55),style=wx.CB_READONLY)
        wx.StaticText(self, label='Set number of Treadles:', pos=(15, 60), size=(200, 45))
        
        self.shedtype = wx.ComboBox(self, choices=LOOM_SHED_TYPE, value=curShedType, pos=(145, 95),style=wx.CB_READONLY)
        wx.StaticText(self, label='Set Shed Type:', pos=(15, 100), size=(120, 45))
        
        okButton = wx.Button(self, wx.ID_OK, "OK", pos=(15, 155))
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(205, 155))
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # self.SetSizer(sizer)
        
    #----------------------------------------------------------------------

class SetWarpThreadsDialog(wx.Dialog):
    """
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Warp Threads")
        ends = []
        for thread in range(4, 130, 4):
            ends.append(str(thread))
        
        self.threadcount = wx.ComboBox(self, choices=ends, value="")
        okBtn = wx.Button(self, wx.ID_OK)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.threadcount, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
        
    #----------------------------------------------------------------------

class SetWeftPickDialog(wx.Dialog):
    """
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Weft Pick")
        ends = []
        for thread in range(4, 130, 4):
            ends.append(str(thread))
        
        self.pickcount = wx.ComboBox(self, choices=ends, value="")
        okBtn = wx.Button(self, wx.ID_OK)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pickcount, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(okBtn, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)
    
#----------------------------------------------------------------------
