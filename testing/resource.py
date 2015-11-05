import wx

'''
keep track of the id
to use in multiple modules
'''
ID_QUIT = wx.NewId()
ID_FILE_OPEN = wx.NewId()
ID_THREADING_GRID = wx.NewId()
ID_TREADLING_GRID = wx.NewId()
ID_TIEUP_GRID = wx.NewId()
ID_DRAWDOWN_GRID = wx.NewId()
ID_ABOUT = wx.NewId()
ID_TOOLS_VIEW_WIF = wx.NewId()

# #----------------------------------------------------------------------

SHAFTS = 8
ENDS = 64
CELL_SIZE = 20
# #----------------------------------------------------------------------

WIF_SECTION_COMMENT = "Comment"
WIF_SECTION_WIF = "Wif"
WIF_SECTION_CONTENTS = "Contents"
WIF_SECTION_COLOR_PALETTE = "Color Palette"
WIF_SECTION_WARP_SYMBOL_PALETTE = "Warp Symbol Palette"
WIF_SECTION_WEFT_SYMBOL_PALETTE = "Weft Symbol Palette"
WIF_SECTION_TEXT = "Text"
WIF_SECTION_WEAVING = "Weaving"
# WARP=
# WEFT=
WIF_SECTION_WARP = "Warp"
WIF_SECTION_WEFT = "Weft"
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
# #----------------------------------------------------------------------

# ID_QUIT = wx.NewId()
# ID_ABOUT = wx.NewId()
# ID_MAINTAIN_BARCODES = wx.NewId()
# ID_REPORTS = wx.NewId()
# ID_PREFERENCES = wx.NewId()
# ID_OPEN_PREFERENCES = wx.NewId()
# ID_MAINTAIN_BARCODES_QUIT = wx.NewId()
# ID_MAINTAIN_BARCODES_LIST = wx.NewId()
# ID_BARCODE_CATEGORY = wx.NewId()
# ID_BARCODE_ADD = wx.NewId()
# ID_BARCODE_LIST = wx.NewId()
# ID_BARCODE_ADD_UPDATE = wx.NewId()
# ID_TRAITS = wx.NewId()
# ID_FILE_OPEN = wx.NewId()
# ID_CLEAR_BARCODE = wx.NewId()
# ID_PROCESS_BARCODE_SCANN = wx.NewId()
# ID_CLEAR_BARCODE_SCANN = wx.NewId()
# ID_BARCODE_SCANN_NOTES = wx.NewId()
# ID_NOTES_LIST = wx.NewId()

# # barcode
# DEL_LAST_ENTRY_CODE = "80001"
# RULER_PREFIX = "fb#"

# # barcode categories
# DAY_CATEGORY = 5
# MONTH_CATEGORY = 4
# YEAR_CATEGORY = 3
# NAME_CATEGORY = 6
# LOCATION_CATEGORY = 8
# TREE_CATEGORY = 1
# SCANNER_CATEGORY = 7

# TRAIT_CATEGORY = 10
# VALUE_CATEGORY = 15

# SCAN_WIDE_VALUE = 1

# # traits comboboxes
# COLLECTION_TIMES_LIST = ['Bloom', 'Dormant', 'Growing', 'Harvest']
# DATA_TYPES_LIST = ['Binary', 'Nominal', 'Ordinal', 'Quantitative']
# UNITS_LIST = ['Percent', 'mm', 'cm', 'meter', 'inch', 'foot', 'Count']
# PLANT_PART_LIST = ['Flower', 'Fruit', 'Leaf', 'Petiol','Shoot', 'Tree' ]
# PRINT_BARCODES_COLUMNS = ['1','2','3','4']
