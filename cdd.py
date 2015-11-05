#!/usr/bin/env python

import wx
import wx.grid as gridlib
import os
import string

from resource import *
from WIF import *


# #----------------------------------------------------------------------


#----------------------------------------------------------------------

class ShowWeavingInfoFile(wx.Dialog):

    def __init__(self, *args, **kw):
        super(ShowWeavingInfoFile, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((250, 200))


    def InitUI(self):

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(pnl, label='Colors')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(pnl, label='256 Colors', style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(pnl, label='16 Colors'))
        sbs.Add(wx.RadioButton(pnl, label='2 Colors'))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(pnl, label='Custom'))
        hbox1.Add(wx.TextCtrl(pnl), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)


    def OnClose(self, e):

        self.Destroy()

#----------------------------------------------------------------------
#----------------------------------------------------------------------

#----------------------------------------------------------------------
class CDDconfig(object):
    def __init__(self):
        # lastdir=/home/scott/projects/weaving/cannwoven/data
        # sizewidth=800
        # sizeheight=600
        # positionleft=100
        # positiontop=100
        # file0=path/filename
        # file1=ojsjflahsdf
        # file2=
        # file3=
        # file4=
        self.ConfigFile = os.getcwd() + "/cdd.ini"
        self.LastDir = os.getcwd()
        self.SizeWidth = 800
        self.SizeHeight = 600
        self.PositionLeft = 100
        self.PositionTop = 100
        self.RecentWIF = []

    def AddRecentWIFFile(self, filename):
        # bump the file list insert the current
        # only saving last five
        self.RecentWIF.insert(0, filename)

    def get(self):
        # open file and get last dir and size
        myFile = open(self.ConfigFile,'r')
        for line in iter(myFile):
            # print cur_line
            cur_line = line.rstrip('\r\n')
            if bool(cur_line):
                if (cur_line[0:7] == "lastdir"):
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    self.LastDir = value
                elif (cur_line[0:9] == "sizewidth"):
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    self.SizeWidth = int(value)
                elif (cur_line[0:10] == "sizeheight"):
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    self.SizeHeight = int(value)
                elif (cur_line[0:12] == "positionleft"):
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    self.PositionLeft = int(value)
                elif (cur_line[0:11] == "positiontop"):
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    self.PositionTop = int(value)
                elif (cur_line[0:4] == "file"):
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    self.RecentWIF.append(value)
                else:
                    pass

        myFile.close()

    def set(self):
        # open file and write lastdir and  size
        myFile = open(self.ConfigFile,'w')
        lastdir = "lastdir=" + self.LastDir + "\n"
        myFile.write(lastdir)
        sw = "sizewidth=" + str(self.SizeWidth)  + "\n"
        myFile.write(sw)
        sh = "sizeheight="+ str(self.SizeHeight)  + "\n"
        myFile.write(sh)
        pl = "PositionLeft=" + str(self.PositionLeft)  + "\n"
        myFile.write(pl)
        pt = "positiontop=" + str(self.PositionTop)  + "\n"
        myFile.write(pt)
        file_count = len(self.RecentWIF)
        # only save last five files
        if file_count > 5:
            file_count = 5
        for fileindex in range(file_count):
            # print self.RecentWIF[fileindex], fileindex
            filewif = "file" + str(fileindex) + "=" + self.RecentWIF[fileindex] + "\n"
            myFile.write(filewif)
        myFile.close()


#----------------------------------------------------------------------
class myFileDialog(wx.FileDialog):
    def __init__(self, parent):
        wx.FileDialog.__init__(self, parent)

    def ShowModal(self, lastdir):
        # need last dir
        filters = 'WIF files (*.wif)|*.wif'
        dialog = wx.FileDialog ( None, message = 'Weaving Information File (WIF)', wildcard = filters, style = wx.OPEN )
        # dialog = wx.FileDialog ( None, message = 'Weaving Information File (WIF)', wildcard = filters, defaultDir=os.getcwd(), style = wx.OPEN )
        dialog.SetDirectory(lastdir)
        if dialog.ShowModal() == wx.ID_OK:
            return dialog.GetPath()
        else:
            return None
#----------------------------------------------------------------------


class CannsDrawDownApp(wx.App):
	"""The wx.App for the wxHello application"""

	def OnInit(self):
            """Override OnInit to create our Frame"""
            self.CannDrawDownFrame = wx.Frame(None, title="wxHello")
            self.CannDrawDownFrame.Show()
            self.SetTopWindow(self.CannDrawDownFrame)
            return True

class MyForm(wx.Frame):

    def __init__(self):
        self.canndrawWin = wx.Frame.__init__(self, None, wx.ID_ANY, "Canns DrawDown",  size=(800,600))
        # pos=(100,100),
        self.wif_file_name = ""

        self.CDDConfig = CDDconfig()
        self.CDDConfig.get()
        self.last_dir = self.CDDConfig.LastDir
        left = int(self.CDDConfig.PositionLeft)
        top = int(self.CDDConfig.PositionTop)
        # print "left, top", left, top
        width = int(self.CDDConfig.SizeWidth)
        height = int(self.CDDConfig.SizeHeight)
        # print "width, height" , width, height
        # self.MoveXY(left, top)
        # self.SetPosition
        # self.SetDimensions(x, y, width, height, sizeFlags)
        self.SetDimensions(left, top, width, height)

        # file_count = len(self.CDDConfig.RecentWIF)
        # for fileindex in range(file_count):
        #     print self.CDDConfig.RecentWIF[fileindex], fileindex

        self.wif = Weaving_Info_File()
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.InitUI()
        # self.Centre()
        self.Show()

    def InitUI(self):
        self.Create_Menu()
        self.Create_Layout()

    def Create_Menu(self):
        # resently open files?
        menubar = wx.MenuBar()
        filem = wx.Menu()
        recentm = wx.Menu()
        editm = wx.Menu()
        toolsm = wx.Menu()
        helpm = wx.Menu()
        recentfilesm = wx.Menu()

        menubar.Append(filem, '&File')
        open_file = wx.MenuItem(filem, ID_FILE_OPEN, '&Open WIF File')
        open_file.SetBitmap(wx.Image('document-open.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())

        for file in self.CDDConfig.RecentWIF:
            recentfilesm.Append(ID_RECENT_FILES, file)
            # self.Bind(wx.EVT_MENU, partial(self.Load_File, 1), menu_item_1)

        # recent_files = wx.MenuItem(recentm, ID_RECENT_FILES, 'Recent WIF Files')
        quit = wx.MenuItem(filem, ID_QUIT, '&Quit\tCtrl+W')
        quit.SetBitmap(wx.Image('application-exit.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        filem.AppendItem(open_file)
        filem.AppendSeparator()

        recent_files = filem.AppendMenu(wx.ID_ANY, 'Recent WIF Files', recentfilesm)
        # recent_files = wx.MenuItem(recentm, wx.ID_ANY, 'Recent WIF Files')
        # recent_files.SetBitmap(wx.Image('document-open-recent.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        # recent_files.AppendMenu(recentfilesm)
        # filem.AppendItem(recent_files)

        filem.AppendSeparator()
        filem.AppendItem(quit)

        self.Bind(wx.EVT_MENU, self.OnOpenFile, id=ID_FILE_OPEN)
        #self.Bind(wx.EVT_MENU, self.OnOpenFile, id=ID_RECENT_FILES)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=ID_QUIT)

        menubar.Append(editm, '&Edit')

        menubar.Append(toolsm, '&Tools')
        view_wif = wx.MenuItem(toolsm, ID_TOOLS_VIEW_WIF, '&View WIF File')
        toolsm.AppendItem(view_wif)
        self.Bind(wx.EVT_MENU, self.OnViewWIF, id=ID_TOOLS_VIEW_WIF)

        helpm.Append(ID_ABOUT, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=ID_ABOUT)

        menubar.Append(helpm, '&Help')

        self.SetMenuBar(menubar)

    def OnAboutBox(self, event):
        '''
        display an about message
        '''
        description = """Canns DrawDown.\n\nCreater - Scott L. Cann\nCopyright - Scott L. Cann 2015"""
        dlg = wx.MessageDialog(self, description, "About", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        event.Skip()

    def OnViewWIF(self, event):
        '''
        display an WIF file
        '''
        if self.wif_file_name == "":
            event.Skip()
            pass
        print "|" + self.wif_file_name + "|"

        chgdep = ShowWeavingInfoFile(None, title='Show WIF')
        chgdep.ShowModal()
        chgdep.Destroy()

        # description = """WIF file \n""" + self.wif_file_name
        # dlg = wx.MessageDialog(self, description, "WIF File", wx.OK | wx.ICON_INFORMATION)
        # dlg.ShowModal()
        # dlg.Destroy()
        event.Skip()

    def OnQuit(self, event):
        '''
        save the position and size of the main app frame
        '''
        #self.config.save_position()
        self.CDDConfig.LastDir = self.last_dir
        top, left = self.GetScreenPositionTuple()
        width, height =  self.GetSizeTuple()
        self.CDDConfig.PositionLeft = left
        self.CDDConfig.PositionTop = top
        self.CDDConfig.SizeWidth = width
        self.CDDConfig.SizeHeight = height
        # print "top", top, "left", left
        # print "width", width, "height", height
        self.CDDConfig.set()
        self.Destroy()

    def OnOpenFile(self, event):
        #
        open_file = myFileDialog(self)
        wif_file = open_file.ShowModal(self.last_dir)
        # self.wif_file_name = open_file.ShowModal(self.last_dir)
        self.CDDConfig.AddRecentWIFFile(wif_file)
        self.last_dir = os.path.dirname(wif_file)
        # print self.last_dir
        if wif_file == None:
            wx.MessageBox("No WIF file selected")
        else:
            self.Load_WIF_File(wif_file)
            # print "File name", self.wif_file_name
            # # self.canndrawWin.SetTitle(self.wif_file_name)
            # self.wif.clear_wif()
            # self.wif.read_wif(self.wif_file_name)
            # file_lines = ""
            # file_lines += "Version: " + self.wif.Version + "\n"
            # file_lines += "Developers: " + self.wif.Developers + "\n"
            # # print wif.contents
            # print self.wif.weaving
            # print self.wif.warp
            # # file_lines += self.wif.warp
            # # file_lines += self.wif.weft
            # #for thr in wif.threading.threads:
            # #    print thr, wif.threading.threads[thr].Shaft, wif.threading.threads[thr].Color

            # # self.tc3.SetValue(file_lines)
            # self.Create_Layout()
            # self.Load_Grids()

            # msg = wx.grid.GridTableMessage(self,          # The table
            #                                wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
            #                                1                                       # how many
            #                            )
            # self.GetView().ProcessTableMessage(msg)
        event.Skip()

    def Load_WIF_File(self, wif_file):
        self.wif_file_name = wif_file
        # print "File name", self.wif_file_name
        # self.canndrawWin.SetTitle(self.wif_file_name)
        self.wif.clear_wif()
        self.wif.read_wif(self.wif_file_name)
        file_lines = ""
        file_lines += "Version: " + self.wif.Version + "\n"
        file_lines += "Developers: " + self.wif.Developers + "\n"

        print self.wif.weaving
        print self.wif.warp

        self.Create_Layout()
        self.Load_Grids()

    def Load_Grids(self):
        # -----------------------------------------------------------------------
        # threading
        # load threading
        # self.wif.threading
        # self.wif.threading.threads[1].Shaft or Color
        for thread in self.wif.threading.threads:
            # print thread, self.wif.threading.threads[thread].Shaft
            col = thread - 1
            row = self.wif.weaving.Shafts - self.wif.threading.threads[thread].Shaft
            shaft = str(self.wif.threading.threads[thread].Shaft)
            # print row, col, shaft
            if(shaft == "0"):
                pass
            else:
                # print "Threading row col", row, col
                self.threading_grid.SetCellBackgroundColour(row, col, wx.BLACK)
                self.threading_grid.SetCellTextColour(row, col, wx.WHITE)
                self.threading_grid.SetCellValue(row, col, shaft)

        # self.threading_grid
        # self.threading_grid.SetCellBackgroundColour(row, col, wx.BLACK)
        # self.threading_grid.SetCellTextColour(row, col, wx.WHITE)
        # self.threading_grid.SetCellValue(row, col, harness)

        # -----------------------------------------------------------------------
        # load tie up
        # self.wif.tieup
        # self.tie_up_grid

        for treadle in self.wif.tieup.treadle:
            # print "Tie up", tie, self.wif.tieup.treadle[treadle]
            for cur_shaft in self.wif.tieup.treadle[treadle]:
                # print cur_shaft
                col = treadle - 1
                row = self.wif.weaving.Shafts - cur_shaft
                shaft = str(cur_shaft)
                if(shaft == "0"):
                    pass
                else:
                    self.tie_up_grid.SetCellBackgroundColour(row, col, wx.BLACK)
                    self.tie_up_grid.SetCellTextColour(row, col, wx.WHITE)
                    self.tie_up_grid.SetCellValue(row, col, shaft)


        # -----------------------------------------------------------------------
        # load treadling
        # self.wif.treadling
        # self.treadling_grid
        for pick in self.wif.treadling.treadles:
            # print "treadle", pick, self.wif.treadling.treadles[pick].treadle
            row = pick - 1
            col = self.wif.treadling.treadles[pick].treadle - 1
            shaft = str(self.wif.treadling.treadles[pick].treadle)
            if(shaft == "0"):
                pass
            else:
                self.treadling_grid.SetCellBackgroundColour(row, col, wx.BLACK)
                self.treadling_grid.SetCellTextColour(row, col, wx.WHITE)
                self.treadling_grid.SetCellValue(row, col, shaft)

        # -----------------------------------------------------------------------
        # do drawdown
        # self.drawdown_grid
        # loop through treadles
        for pick in self.wif.treadling.treadles:
            # print "pick| treadle", pick, self.wif.treadling.treadles[pick].treadle
            treadle = self.wif.treadling.treadles[pick].treadle
            row = pick - 1
            #    loop through tie-up
            for tie_up_shaft in self.wif.tieup.treadle[treadle]:
                #       get shafts
                # print "shaft", tie_up_shaft
                #       loop through threads
                for thread in self.wif.threading.threads:
                    #          if shaft make mark
                    col = thread - 1
                    if (tie_up_shaft == self.wif.threading.threads[thread].Shaft):
                        # print self.wif.threading.threads[thread].Shaft
                        self.drawdown_grid.SetCellBackgroundColour(row, col, wx.BLACK)

    def Create_Layout(self):
        curShafts = SHAFTS + 1
        curEnds = ENDS
        curTreadles = SHAFTS
        curPicks = ENDS

        # Add a panel so it looks the correct on all platforms
        self.panel.SetBackgroundColour('#4f5049')

        main_box = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(rows=2, cols=2, hgap=2, vgap=2)
        # fgs.SetFlexibleDirection( wx.HORIZONTAL )
        # fgs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        # threading

        print "Shafts ", self.wif.weaving.Shafts
        print "Threads ", self.wif.warp.Threads

        if (self.wif.weaving.Shafts > 0) and (self.wif.warp.Threads > 0):
            self.threading_grid.Destroy()
            self.tie_up_grid.Destroy()
            self.treadling_grid.Destroy()
            self.drawdown_grid.Destroy()

            curShafts = self.wif.weaving.Shafts
            curEnds = self.wif.warp.Threads
            curPicks = self.wif.weft.Threads
            curTreadles = self.wif.weaving.Treadles


        if (self.wif.warp.Threads < 100):
            CellSize = CELL_SIZE_10
        elif(self.wif.warp.Threads < 1000):
            CellSize = CELL_SIZE_100
        else:
            CellSize = CELL_SIZE_1000
        # -----------------------------------------------------------------------
        # threading
        self.threading_grid = gridlib.Grid(self.panel, ID_THREADING_GRID)

        self.threading_grid.CreateGrid(curShafts, curEnds)


        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick, id=ID_THREADING_GRID)
        # no row labels
        self.threading_grid.SetRowLabelSize(0)
        # show thread count
        self.threading_grid.SetColLabelSize(CellSize)

        # print  wx.BLACK
        # self.threading.colour[7] = wx.CYAN

        # set col size
        # and add the thread colour row on the top row
        for c in xrange(self.threading_grid.GetNumberCols()):
            self.threading_grid.SetColSize(c, CellSize)
            # self.threading_grid.SetCellBackgroundColour(0, c, self.threading.threads[c].colour)
            self.threading_grid.SetCellTextColour(0, c, wx.BLACK)
            col = str(c + 1)
            self.threading_grid.SetColLabelValue(c, col)

        for r in xrange(self.threading_grid.GetNumberRows()):
            self.threading_grid.SetRowSize(r, CellSize)

        self.threading_grid.DisableDragColSize()
        self.threading_grid.DisableDragRowSize()

        # -----------------------------------------------------------------------
        # tie up
        # Treadles=12
        if (self.wif.weaving.Treadles > 0):
            curTreadles = self.wif.weaving.Treadles
        self.tie_up_grid = gridlib.Grid(self.panel, ID_TIEUP_GRID)

        self.tie_up_grid.CreateGrid(curShafts, curTreadles)

        self.tie_up_grid.SetRowLabelSize(0)
        self.tie_up_grid.SetColLabelSize(CellSize)


        # set col size and label with treadle number
        for c in xrange(self.tie_up_grid.GetNumberCols()):
            self.tie_up_grid.SetColSize(c, CellSize )
            # self.tie_up_grid.SetCellBackgroundColour(row, col, wx.BLACK)
            self.tie_up_grid.SetCellTextColour(0, c, wx.BLACK)
            col = str(c + 1)
            self.tie_up_grid.SetColLabelValue(c, col)

        for r in xrange(self.tie_up_grid.GetNumberRows()):
            self.tie_up_grid.SetRowSize(r, CellSize )

        self.tie_up_grid.DisableDragColSize()
        self.tie_up_grid.DisableDragRowSize()
        # self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnTieupCellLeftClick, id=ID_TIEUP_GRID)
        # self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnTieupCellRightClick, id=ID_TIEUP_GRID)

        # -----------------------------------------------------------------------
        # drawdown grid
        self.drawdown_grid = gridlib.Grid(self.panel, ID_DRAWDOWN_GRID)
        self.drawdown_grid.CreateGrid(curEnds, curPicks)

        self.drawdown_grid.SetRowLabelSize(0)
        self.drawdown_grid.SetColLabelSize(0)
        # set col size
        for c in xrange(self.drawdown_grid.GetNumberCols()):
            self.drawdown_grid.SetColSize(c, CellSize)

        for r in xrange(self.drawdown_grid.GetNumberRows()):
            self.drawdown_grid.SetRowSize(r, CellSize)

        self.drawdown_grid.DisableDragColSize()
        self.drawdown_grid.DisableDragRowSize()

        # -----------------------------------------------------------------------
        # treadling
        self.treadling_grid = gridlib.Grid(self.panel, ID_TREADLING_GRID)
        self.treadling_grid.CreateGrid(curPicks, curTreadles)
        # self.treadles = Treadling(ENDS, SHAFTS + 2)
        self.treadling_grid.SetRowLabelSize(0)
        self.treadling_grid.SetColLabelSize(0)
        # set col size
        for c in xrange(self.treadling_grid.GetNumberCols()):
            self.treadling_grid.SetColSize(c, CellSize)

        for r in xrange(self.treadling_grid.GetNumberRows()):
            self.treadling_grid.SetRowSize(r, CellSize)

        self.treadling_grid.DisableDragColSize()
        self.treadling_grid.DisableDragRowSize()

        # link scroll treadle and drawdown
        self.drawdown_grid.Bind(wx.EVT_SCROLLWIN, self.OnScrollDrawdown)
        self.treadling_grid.Bind(wx.EVT_SCROLLWIN, self.OnScrollTreadle)

        # link scroll treadle and threading
        self.drawdown_grid.Bind(wx.EVT_SCROLLWIN, self.OnHScrollDrawdown)
        self.threading_grid.Bind(wx.EVT_SCROLLWIN, self.OnHScrollThreading)

        # -----------------------------------------------------------------------
        fgs.AddMany([(self.tie_up_grid, 1, wx.EXPAND), (self.threading_grid, 1, wx.EXPAND), (self.treadling_grid, 5, wx.EXPAND),
            (self.drawdown_grid, 5, wx.EXPAND)])


        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 10)
        # fgs.AddGrowableCol(0, 50)
        # fgs.AddGrowableRow(1, 50)
        fgs.AddGrowableCol(1, 10)

        main_box.Add(fgs, proportion=1, flag=wx.ALIGN_CENTRE|wx.ALL|wx.EXPAND, border=2)

        self.panel.SetSizer(main_box)
        self.panel.Layout()

    #----------------------------------------------------------------------


    #----------------------------------------------------------------------
    # link treadle and drawdown grids to scroll together
    def OnScrollDrawdown(self, event):
        if event.Orientation == wx.SB_VERTICAL:
        #     self.treadling_grid.Scroll(event.Position, -1)
        # else:
            self.treadling_grid.Scroll(-1, event.Position)
        event.Skip()

    def OnScrollTreadle(self, event):
        if event.Orientation == wx.SB_VERTICAL:
        #     self.drawdown_grid.Scroll(event.Position, -1)
        # else:
            self.drawdown_grid.Scroll(-1, event.Position)
        event.Skip()

    # link threading and drawdown grids to scroll together horizontally
    def OnHScrollDrawdown(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.threading_grid.Scroll(event.Position, -1)
        else:
            pass
        event.Skip()

    def OnHScrollThreading(self, event):
        if event.Orientation == wx.SB_HORIZONTAL:
            self.drawdown_grid.Scroll(event.Position, -1)
        else:
            pass
        event.Skip()
        # self.drawdown_grid.Bind(wx.EVT_SCROLLWIN, self.OnHScrollDrawdown)
        # self.threading_grid.Bind(wx.EVT_SCROLLWIN, self.OnHScrollThreading)
    #----------------------------------------------------------------------

    # left click on the threading grid to thread the harness
    def OnCellLeftClick(self, evt):
        """
        """
        row = evt.GetRow()
        col = evt.GetCol()
        if (row == 0):
            # colour row
            # change colour on click
            return

        harness = str(self.threading_grid.GetNumberRows() - evt.GetRow())

        if (self.threading.threads[col].harness != -1):
            # reset current and add
            past_harness = self.threading.threads[col].harness
            past_row = self.threading_grid.GetNumberRows() - past_harness
            self.threading_grid.SetCellBackgroundColour(past_row, col, wx.WHITE)
            self.threading_grid.SetCellValue(past_row, col, '')

        # set the harness number in the array
        self.threading.threads[col].harness = int(harness)
        #add the colour of the 0 row
        #self.threading.threads[col].colour = (0,0,0)
        self.threading.threads[col].colour = self.threading_grid.GetCellBackgroundColour(0, col)
        # print self.threading_grid.GetCellBackgroundColour(0, col)
        self.threading_grid.SetCellBackgroundColour(row, col, wx.BLACK)
        self.threading_grid.SetCellTextColour(row, col, wx.WHITE)
        self.threading_grid.SetCellValue(row, col, harness)

        evt.Skip()
    #----------------------------------------------------------------------

    # hook up the peddles to the harness
    def OnTieupCellLeftClick(self, evt):
        row = evt.GetRow()
        col = evt.GetCol()
        # if row == 0:
        #     return

        harness = str(self.tie_up_grid.GetNumberRows() - row)

        self.tie_up_grid.SetCellBackgroundColour(row, col, wx.BLACK)
        self.tie_up_grid.SetCellTextColour(row, col, wx.WHITE)
        self.tie_up_grid.SetCellValue(row, col, "X")

        self.tie_up.peddle[col][row - 1] = harness
        #print self.tie_up.peddle

        evt.Skip()

    # unhook harnes from peddle
    def OnTieupCellRightClick(self, evt):
        row = evt.GetRow()
        col = evt.GetCol()
        # if row == 0:
        #     return

        harness = str(self.tie_up_grid.GetNumberRows() - row)

        self.tie_up_grid.SetCellBackgroundColour(row, col, wx.WHITE)
        self.tie_up_grid.SetCellTextColour(row, col, wx.BLACK)
        self.tie_up_grid.SetCellValue(row, col, "")

        self.tie_up.peddle[col][row - 1] = -1
        # print self.tie_up.peddle

        evt.Skip()

    #----------------------------------------------------------------------

    # not being used
    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu

        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()
    #----------------------------------------------------------------------

# Run the program
if __name__ == "__main__":
    app = CannsDrawDownApp()
    app.MainLoop()
