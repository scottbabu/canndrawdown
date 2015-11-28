import wx

'''
keep track of the id
to use in multiple modules
'''
ID_QUIT = wx.NewId()
ID_FILE_OPEN = wx.NewId()
ID_FILE_CLOSE = wx.NewId()
ID_THREADING_GRID = wx.NewId()
ID_TREADLING_GRID = wx.NewId()
ID_TIEUP_GRID = wx.NewId()
ID_DRAWDOWN_GRID = wx.NewId()
ID_ABOUT = wx.NewId()
ID_TOOLS_VIEW_WIF = wx.NewId()
ID_RECENT_FILES = wx.NewId()
ID_SET_WARP_THREADS = wx.NewId()
ID_SET_WEFT_PICKS = wx.NewId()
ID_SET_SHAFT_COUNT = wx.NewId()
ID_SET_TREADLE_COUNT = wx.NewId()
# #----------------------------------------------------------------------

SHAFTS = 8
ENDS = 64
CELL_SIZE_1 = 18
CELL_SIZE_10 = 20
CELL_SIZE_100 = 30
CELL_SIZE_1000 = 40
# #----------------------------------------------------------------------
APP_NAME = "Canns DrawDown"
APP_VERSION = "1.0"
APP_COPYRIGHT = "(C) 2010 - 2015 Scott Cann"
APP_DEVELOPER = "Scott Cann"
# #----------------------------------------------------------------------

# #----------------------------------------------------------------------
# used in SetShaftCountDialog in cannsdrawdown.py
LOOM_SHAFT_COUNT_LIST = ["2","4","8","12","16","24","30","40"]
LOOM_TREADLE_COUNT_LIST = ["2","4","6","10","12","14","18","24"]
LOOM_SHED_TYPE = ["Jack","Counter Balance","Counter March","Rising Shed","Sinking Shed"]
LOOM_RISING_SHED =  ["Jack","Rising Shed"]
LOOM_SINKING_SHED =  ["Counter Balance","Counter March","Sinking Shed"]

# #----------------------------------------------------------------------
WARP_THREADING = "Straight Draw","Pointed Twill","Rose Path","Broken Twill"
WARP_THREADING_STRAIGHT_DRAW_4 = [1,2,3,4] # repeat for all threads
WARP_THREADING_STRAIGHT_DRAW_8 = [1,2,3,4,5,6,7,8]
WARP_THREADING_STRAIGHT_DRAW_12 = [1,2,3,4,5,6,7,8,9,10,11,12]
WARP_THREADING_STRAIGHT_DRAW_16 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# #----------------------------------------------------------------------
# #----------------------------------------------------------------------
# WIF CONTENTS
WIF_SECTION_COMMENT = "Comment"
WIF_SECTION_WIF = "Wif"

WIF_SECTION_CONTENTS = "Contents"
WIF_VALUE_TRUE = "True"
WIF_VALUE_ON = "On"
WIF_VALUE_YES = "Yes"
WIF_VALUE_ONE = "1"
WIF_VALUE_FALSE = "False"
WIF_VALUE_OFF = "Off"
WIF_VALUE_NO = "No"
WIF_VALUE_ZERO = "0"
WIF_DEFALT_BLACK = 1
WIF_DEFALT_WHITE = 2
WIF_DEFALT_THREAD_COLOUR_BLACK = (0,0,0)
WIF_DEFALT_THREAD_COLOUR_WHITE = (255,255,255)

WIF_SECTION_COLOR_PALETTE = "Color Palette"
WIF_SECTION_COLOR_PALETTE_ENTRIES = "Entries"
WIF_SECTION_COLOR_PALETTE_RANGE = "Range"

WIF_SECTION_WARP_SYMBOL_PALETTE = "Warp Symbol Palette"
WIF_SECTION_WEFT_SYMBOL_PALETTE = "Weft Symbol Palette"
WIF_SECTION_TEXT = "Text"

WIF_SECTION_WEAVING = "Weaving"
# [WEAVING]
# ; information on the weaving
# Shafts=      ;required (integer) ( >0 )
WIF_SECTION_WEAVING_SHAFTS = "Shafts"
# Treadles=    ;required (integer) ( >0 )
WIF_SECTION_WEAVING_TREADLES = "Treadles"
# Rising Shed= ;optional (boolean) ({true,on,yes,1} {false,off,no,0})
WIF_SECTION_WEAVING_RISING_SHED = "Rising Shed"
# ;-   Profile=     ;obsolete (boolean) ({true,on,yes,1} {false,off,no,0})

WIF_SECTION_WARP = "Warp"
WIF_SECTION_WEFT = "Weft"

# WARP=
# Threads=        ;'required (integer) ( >0 )
WIF_SECTION_WARP_WEFT_THREADS = "Threads"
# ;the number of threads in the threading section

# Color=    ;optional  (1 or 4 integers)([Palette Ndx],[R,G,B])
WIF_SECTION_WARP_WEFT_COLOR = "Color"
#           ;{[0<Palette Ndx<=[Color Palette].Entries],
#           ;[Color Palette].Range.From<=RGB<=[Color Palette].Range.To]}
# ; This key can hold two values, Palette Ndx and optional R,G,B.
# ; Palette Ndx is a valid index into the Warp Color Table.
# ; Use the Palette NDX value to initialize the warp threads' color
# ; variable.
# ; Use the optional RGB values for the warp color in two-color drafts.

WIF_SECTION_WARP_WEFT_SYMBOL = "Symbol"
# Symbol=         ;optional (valid WIF symbol data type)
# ; Use for warp symbol in two-symbol drafts

WIF_SECTION_WARP_WEFT_SYMBOL_NUMBER = "Symbol Number"
# Symbol Number=  ;optional (integer) ( >0 )
# ; an index into the Warp Symbol Table
# ; Use to initialize the warp threads' symbol number variable.

WIF_SECTION_WARP_WEFT_UNITS = "Units"
# Units=          ;required if spacing or thickness is used (ASCII String)
#                 ;({"Decipoints","Inches","Centimeters"})
# ; units in which spacing and thickness are measured
WIF_SECTION_WARP_WEFT_UNITS_DECIPOINTS = "Decipoints"
WIF_SECTION_WARP_WEFT_UNITS_INCHES = "Inches"
WIF_SECTION_WARP_WEFT_UNITS_CENTIMETERS = "Centimeters"

WIF_SECTION_WARP_WEFT_SPACING = "Spacing"
# Spacing=        ;optional (real) ( >=0 )
# ; base spacing for warp
# ; Use to initialize the warp threads' spacing variable.

WIF_SECTION_WARP_WEFT_THICKNESS = "Thickness"
# Thickness=      ;optional (real) ( >=0 )
# ; base thickness for warp
# ; Use to initialize the warp threads' thickness variable.

WIF_SECTION_WARP_WEFT_SPACING_ZOOM = "Spacing Zoom"
# Spacing Zoom=   ;optional (integer) ( >=0 )
# ; zoom factor applied to base for variable spacing draft
# ; Use to initialize the warp threads' spacing zoom variable.

WIF_SECTION_WARP_WEFT_THICKNESS_ZOOM = "Thickness Zoom"
# Thickness Zoom= ;optional (integer) ( >=0 )
# ; zoom factor applied to base for variable spacing draft
# ; Use to initialize the warp threads' thickness zoom variable.

# WEFT=
# ;-   bitmap support not implemented but keywords reserved for future
# ;-   BITMAP IMAGE=
# ;-   BITMAP FILE=

# ;Beginning of Data Sections
WIF_SECTION_NOTES = "Notes"
WIF_SECTION_TIEUP = "Tieup"

# ; Color and Symbol tables
WIF_SECTION_COLOR_TABLE = "Color Table"
WIF_SECTION_WARP_SYMBOL_TABLE = "Warp Symbol Table"
WIF_SECTION_WEFT_SYMBOL_TABLE = "Weft Symbol Table"
# ; Warp Data Sections
WIF_SECTION_THREADING = "Threading"
WIF_SECTION_WARP_THICKNESS = "Warp Thickness"
WIF_SECTION_WARP_THICKNESS_ZOOM = "Warp Thickness Zoom"
WIF_SECTION_WARP_SPACING = "Warp Spacing"
WIF_SECTION_WARP_SPACING_ZOOM = "Warp Spacing Zoom"
WIF_SECTION_WARP_COLORS = "Warp Colors"
WIF_SECTION_WARP_SYMBOLS = "Warp Symbols"
# ; Weft Data Sections
WIF_SECTION_TREADLING = "Treadling"
WIF_SECTION_LIFTPLAN = "Liftplan"
WIF_SECTION_WEFT_THICKNESS = "Weft Thickness"
WIF_SECTION_WEFT_THICKNESS_ZOOM = "Weft Thickness Zoom"
WIF_SECTION_WEFT_SPACING = "Weft Spacing"
WIF_SECTION_WEFT_SPACING_ZOOM = "Weft Spacing Zoom"
WIF_SECTION_WEFT_COLORS = "Weft Colors"
WIF_SECTION_WEFT_SYMBOLS = "Weft Symbols"

# #----------------------------------------------------------------------
CLEAR_INT = -1
CLEAR_STR = ""
CLEAR_FLOAT = 0.0
OK = 1
# #----------------------------------------------------------------------
