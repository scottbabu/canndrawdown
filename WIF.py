from resource import *

'''
WIF main file and all the other classes
to process the file

things needed
- case insensetivity
-
'''
# def get_value(config, section, key):
#     try:
#         sv = config.get(section,key)
#         return sv
#     except ConfigParser.NoSectionError:
#         return CLEAR_INT
#     except ConfigParser.NoOptionError:
#         return CLEAR_INT


class WIF(object):
    '''
    '''
    def __init__(self):
        self.wif = {"Section":{"Key":"Value"}}

    def clear(self):
        type(self.wif)()
        self.wif = {"Section":{"Key":"Value"}}

    def Read(self, wif_name):
        # open file read each line into a list then close file
        #
        line_num = 0
        current_section = ""

        fh = open(wif_name, "r")
        # strip off carrage return and line feed
        # for cur_line in fh.read().split('\r\n'):
        # for cur_line in fh.read():
        for line in iter(fh):
            # print cur_line
            cur_line = line.rstrip('\r\n')
            # print cur_line
            # check for blank line
            if bool(cur_line):
                # parse into wif structure
                # section , comment, or key/value
                if (cur_line[0] == ";"):
                    # comment
                    # if its not there create it
                    if WIF_SECTION_COMMENT in self.wif.keys():
                        self.wif[WIF_SECTION_COMMENT][line_num] = cur_line
                    else:
                        self.wif.update({WIF_SECTION_COMMENT:{line_num:cur_line}})
                elif (cur_line[0] == "["):
                    # section
                    # remove braces and change from the current cAsE to 'Title Case'
                    current_section = cur_line.replace("[","").replace("]","").title()
                    self.wif.update({current_section:{None:None}})
                    # print "Section", current_section
                else:
                    # key/value and everything else
                    index = cur_line.find("=")
                    key = cur_line[0:index]
                    value = cur_line[index+1:]
                    # key, value = cur_line.split("=")
                    # print cur_line, key, value
                    self.wif[current_section][key.title()] = value
            else:
                # blank line
                # print "blank line", cur_line
                pass

            line_num = line_num + 1
        fh.close()

    def get(self, section, key):
        '''
        from the list self.wif get the value from section key
        '''
        num = 0
        if section in self.wif:
            if key in self.wif[section]:
                return self.wif[section][key]
            else:
                # if the key isn't there
                return None
        else:
            # if the section isn't there
            return None

    def get_boolean(self, section, key):
        '''
        from the list self.wif get the value from section key
        and return boolean True or False
        '''
        num = 0
        if section in self.wif:
            if key in self.wif[section]:
                curVal = str(self.wif[section][key])
                if (curVal.upper() == "TRUE"):
                    return True
                elif (curVal.upper() == "ON"):
                    return True
                elif (curVal.upper() == "YES"):
                    return True
                elif (curVal.upper() == "1"):
                    return True
            else:
                # if nothing on the list (true, on, yes, 1) is found
                return False
        else:
            # if section can't be found
            return False

    def get_int(self, section, key):
        '''
        from the list self.wif get the value from section key
        '''
        num = 0
        if section in self.wif:
            if key in self.wif[section]:
                return int(self.wif[section][key])
            else:
                return CLEAR_INT
        else:
            return CLEAR_INT

    def items(self, section=None):
        '''
        return all the keys in the section
        '''
        if (section == None):
            return self.wif.keys()
        else:
            return self.wif[section].keys()


class Weaving_Info_File(object):
    '''
    the whole file
    '''
    def __init__(self):
        self.config = WIF()

        self.Version = ""
        self.Date = ""
        self.Developers = ""
        self.Source_Program = ""
        self.Source_Version = ""
        self.contents = {}
        self.clear_contents()
        self.weaving = Weaving()
        self.warp = Warp_Weft(WIF_SECTION_WARP)
        self.weft = Warp_Weft(WIF_SECTION_WEFT)
        self.color_palette = Color_Palette()
        self.tieup = Tie_Up()
        self.threading = Threading()
        self.treadling = Treadling()
        self.liftplan = Liftplan()

    def read_wif(self, filename):
        '''
        '''
        self.config.Read(filename)

        self.Version = self.config.get(WIF_SECTION_WIF,'Version')
        self.Date = self.config.get(WIF_SECTION_WIF,'Date')
        self.Developers = self.config.get(WIF_SECTION_WIF,'Developers')
        self.Source_Program = self.config.get(WIF_SECTION_WIF,'Source Program')
        sv = self.config.get(WIF_SECTION_WIF,'Source Version')
        if (sv != None):
            self.Source_Version = sv

        # for key in self.config.wif:
        #     print key, "|"
        self.get_contents()
        # self.contents = self.get_contents()
        # print self.contents

        # if contents list has key set to true then
        # get the data from that section
        if self.contents[WIF_SECTION_WEAVING] == True:
            self.weaving.get(self.config)
        # --------------------------------- done
        if self.contents[WIF_SECTION_WARP] == True:
            self.warp.get(self.config)
        # --------------------------------- done-
        if self.contents[WIF_SECTION_WEFT] == True:
            self.weft.get(self.config)
        # ---------------------------------- done
        # optional
        if self.contents[WIF_SECTION_COLOR_PALETTE] == True:
            self.color_palette.get(self.config)
        else:
            # set default colours
            self.color_palette.set_default_colours()
        # ---------------------------------done
        if self.contents[WIF_SECTION_TIEUP] == True:
            ret = self.tieup.get(self.config, self.weaving.Treadles, self.weaving.Shafts)
            if ret == None:
                print "Error in WIF Tieup"
                # exit from WIF ?
            # print self.tieup.treadle
        # ---------------------------------done
        if self.contents[WIF_SECTION_THREADING] == True:
            ret = self.threading.get(self.config, self.warp.Threads, self.weaving.Shafts, self.color_palette.Entries, self.contents[WIF_SECTION_WARP_COLORS])
            if ret == None:
                print "Error in WIF Threading"
            # need to figure off a way to handle 11722.wif liftplan there is no color for threads
            # print self.threading.threads
        # ---------------------------------done
        # print self.contents[WIF_SECTION_TREADLING]
        if self.contents[WIF_SECTION_TREADLING] == True:
            ret = self.treadling.get(self.config, self.weft.Threads, self.weaving.Treadles, self.color_palette.Entries, self.contents[WIF_SECTION_WEFT_COLORS])
            if ret == None:
                print "Error in WIF Treadling"
            # print self.treadling.treadles
        # ---------------------------------done
        if self.contents[WIF_SECTION_LIFTPLAN] == True:
            ret = self.liftplan.get(self.config, self.weft.Threads, self.weaving.Shafts)
            if ret == None:
                print "Error in WIF Liftplan"
            # print self.liftplan.lift
        # ---------------------------------


    def clear_wif(self):
        '''
        '''
        self.config = CLEAR_STR
        self.config = WIF()

        self.Version = CLEAR_STR
        self.Date = CLEAR_STR
        self.Developers = CLEAR_STR
        self.Source_Program = CLEAR_STR
        self.Source_Version = CLEAR_STR
        # self.contents = {}
        self.clear_contents()
        del(self.weaving)
        self.weaving = Weaving()
        del(self.warp)
        self.warp = Warp_Weft(WIF_SECTION_WARP)
        del(self.weft)
        self.weft = Warp_Weft(WIF_SECTION_WEFT)
        del(self.color_palette)
        self.color_palette = Color_Palette()
        del(self.tieup)
        self.tieup = Tie_Up()
        del(self.threading)
        self.threading = Threading()
        del(self.treadling)
        self.treadling = Treadling()
        del(self.liftplan)
        self.liftplan = Liftplan()

    def clear(self, collection):
        '''
        clears any collection
        '''
        return type(collection)()

    def write_wif(self, filename):
        '''
        '''
        pass


    def get_contents(self):
        for key in self.config.wif[WIF_SECTION_CONTENTS]:
            curVal = False
            curVal = self.config.get_boolean(WIF_SECTION_CONTENTS, key)
            # print key
            self.contents[key] = curVal

    def clear_contents(self):
        self.contents[WIF_SECTION_COLOR_PALETTE] = False
        self.contents[WIF_SECTION_WARP_SYMBOL_PALETTE] = False
        self.contents[WIF_SECTION_WEFT_SYMBOL_PALETTE] = False
        self.contents[WIF_SECTION_TEXT] = False
        self.contents[WIF_SECTION_WEAVING] = False
        self.contents[WIF_SECTION_WARP] = False
        self.contents[WIF_SECTION_WEFT] = False
        self.contents[WIF_SECTION_NOTES] = False
        self.contents[WIF_SECTION_TIEUP] = False
        self.contents[WIF_SECTION_COLOR_TABLE] = False
        self.contents[WIF_SECTION_WARP_SYMBOL_TABLE] = False
        self.contents[WIF_SECTION_WEFT_SYMBOL_TABLE] = False
        self.contents[WIF_SECTION_THREADING] = False
        self.contents[WIF_SECTION_WARP_THICKNESS] = False
        self.contents[WIF_SECTION_WARP_THICKNESS_ZOOM] = False
        self.contents[WIF_SECTION_WARP_SPACING] = False
        self.contents[WIF_SECTION_WARP_SPACING_ZOOM] = False
        self.contents[WIF_SECTION_WARP_COLORS] = False
        self.contents[WIF_SECTION_WARP_SYMBOLS] = False
        self.contents[WIF_SECTION_TREADLING] = False
        self.contents[WIF_SECTION_LIFTPLAN] = False
        self.contents[WIF_SECTION_WEFT_THICKNESS] = False
        self.contents[WIF_SECTION_WEFT_THICKNESS_ZOOM] = False
        self.contents[WIF_SECTION_WEFT_SPACING] = False
        self.contents[WIF_SECTION_WEFT_SPACING_ZOOM] = False
        self.contents[WIF_SECTION_WEFT_COLORS] = False
        self.contents[WIF_SECTION_WEFT_SYMBOLS] = False


class Weaving(object):
    def __init__(self):
        self.Shafts = 0
        self.Treadles = 0
        self.Rising_Shed = False
        # WEAVING
        # Shafts=4
        # Treadles=4
        # Rising Shed=true
    def __str__(self):
        return str(self.Shafts) + " harnesses " + str(self.Treadles) + " treadles " + "Rising Shed is " + str(self.Rising_Shed)

    def get(self, config):
        self.Shafts = config.get_int(WIF_SECTION_WEAVING, WIF_SECTION_WEAVING_SHAFTS)
        self.Treadles = config.get_int(WIF_SECTION_WEAVING, WIF_SECTION_WEAVING_TREADLES)
        self.Rising_Shed = config.get_boolean(WIF_SECTION_WEAVING,WIF_SECTION_WEAVING_RISING_SHED)


# WARP
class Warp_Weft(object):
    def __init__(self, ww_type):
        self.ww_type = ww_type
        self.Threads = 0       # ;required (integer) ( >0 )
        self.Color = 0         # ;optional  (1 or 4 integers)([Palette Ndx],R,G,B)
        self.Symbol = 0        # ;optional (valid WIF symbol data type)
        self.Symbol_Number = 0 # ;optional (integer) ( >0 )
        self.Units = ""        # ;required if spacing or thickness is used (ASCII String)
        #                 ;({"Decipoints","Inches","Centimeters"})
        self.Spacing = 0.0     # ;optional (real) ( >=0 )
        self.Thickness = 0.0   # ;optional (real) ( >=0 )
        self.Spacing_Zoom = 0  # ;optional (integer) ( >=0 )
        self.Thickness_Zoom = 0 # ;optional (integer) ( >=0 )

    def __str__(self):
        return self.ww_type + " " + str(self.Threads) + " Threads"

    def clear(self):
        self.Threads = CLEAR_INT
        self.Color = CLEAR_INT
        self.Symbol = CLEAR_INT
        self.Symbol_Number = CLEAR_INT
        self.Units = CLEAR_STR
        self.Spacing = CLEAR_FLOAT
        self.Thickness = CLEAR_FLOAT
        self.Spacing_Zoom = CLEAR_INT
        self.Thickness_Zoom = CLEAR_INT

    def get(self, config):
        self.Threads = config.get_int(self.ww_type,WIF_SECTION_WARP_WEFT_THREADS)
        # self.Threads = threads

        # color = get_value(config, self.ww_type,'Color')
        color = config.get(self.ww_type, WIF_SECTION_WARP_WEFT_COLOR)
        if (color != None):
            self.Color = color

        units = str(config.get(self.ww_type, WIF_SECTION_WARP_WEFT_UNITS))
        # units = get_value(config, self.ww_type,'Units')
        #  ;({"Decipoints","Inches","Centimeters"})
        if (units != None):
            if (units.title() == WIF_SECTION_WARP_WEFT_UNITS_DECIPOINTS):
                self.Units = WIF_SECTION_WARP_WEFT_UNITS_DECIPOINTS
            elif (units.title() == WIF_SECTION_WARP_WEFT_UNITS_INCHES):
                self.Units = WIF_SECTION_WARP_WEFT_UNITS_INCHES
            elif (units.title() == WIF_SECTION_WARP_WEFT_UNITS_CENTIMETERS):
                self.Units = WIF_SECTION_WARP_WEFT_UNITS_CENTIMETERS


        spacing = config.get(self.ww_type,WIF_SECTION_WARP_WEFT_SPACING)
        # spacing = get_value(config, self.ww_type,'Spacing')
        if (spacing != None):
            self.Spacing = spacing

        # symbol = get_value(config, self.ww_type,'Symbol')
        symbol = config.get(self.ww_type,WIF_SECTION_WARP_WEFT_SYMBOL)
        if (symbol != None):
            self.Symbol = symbol

        symbol_number = config.get_int(self.ww_type,WIF_SECTION_WARP_WEFT_SYMBOL_NUMBER)
        # symbol_number = get_value(config, self.ww_type,'Symbol Number')
        if (symbol_number != CLEAR_INT):
            self.Symbol_Number = symbol_number

        thickness = config.get(self.ww_type,WIF_SECTION_WARP_WEFT_THICKNESS)
        # thickness = get_value(config, self.ww_type,'Thickness')
        if (thickness != None):
            self.Thickness = thickness

        spacing_zoom = config.get_int(self.ww_type,WIF_SECTION_WARP_WEFT_SPACING_ZOOM)
        # spacing_zoom = get_value(config, self.ww_type,'Spacing Zoom')
        if (spacing_zoom != CLEAR_INT):
            self.Spacing_Zoom = spacing_zoom

        thickness_zoom = config.get_int(self.ww_type,WIF_SECTION_WARP_WEFT_THICKNESS_ZOOM)
        # thickness_zoom = get_value(config, self.ww_type,'Thickness Zoom')
        if (thickness_zoom != CLEAR_INT):
            self.Thickness_Zoom = thickness_zoom


        # COLOR PALETTE
        # Entries=3
        # Range=0,255

class Color_Palette(object):
    def __init__(self):
        self.Entries = 0
        self.Range = []
        self.Color_Table = []

    def get(self, config):

        entries = config.get_int(WIF_SECTION_COLOR_PALETTE, WIF_SECTION_COLOR_PALETTE_ENTRIES)
        # entries = get_value(config, WIF_SECTION_COLOR_PALETTE, 'Entries')
        if (entries != None):
            self.Entries = entries

        colour_range = config.get(WIF_SECTION_COLOR_PALETTE, WIF_SECTION_COLOR_PALETTE_RANGE)
        # colour_range = get_value(config, WIF_SECTION_COLOR_PALETTE, 'Range')
        if (colour_range != None):
            # possible values
            # 0,255
            # 0,65535
            # 0,999

            # create list of two values - lower and upper
            self.Range = [int(n) for n in colour_range.split(',')]


        for num in range(0,  self.Entries):
            strEntry = str(num + 1) # for the wif section/key
            intEntry = int(num + 1) # for the list index

            # get the value
            strRGB = config.get(WIF_SECTION_COLOR_TABLE, strEntry)

            # convert rgb string from wif to integer list
            rgb = [int(n) for n in strRGB.split(',')]
            # print rgb
            # check if values are within the lower and upper range of self.Range
            x = True
            for i in rgb:
                if (i <= self.Range[1]) and (i >= self.Range[0]):
                    # ok
                    # print "top = ", self.Range[1], "| bottom = ", self.Range[0], "|", i
                    pass
                else:
                    x = False
            if (x == True):
                # convert above list into tuple
                trgb = tuple(rgb)

                # create instance of Color_Entry of rgb
                tmpEntry = Color_Entry(intEntry, trgb)

                # add to list
                self.Color_Table.append(tmpEntry)

    def set_default_colours(self):
        self.Entries = 2
        self.Range = [0,255]
        # black = tuple([0,0,0])
        blackEntry = Color_Entry(WIF_DEFALT_BLACK, WIF_DEFALT_THREAD_COLOUR_BLACK)
        self.Color_Table.append(blackEntry)
        # white = tuple([255,255,255])
        whiteEntry = Color_Entry(WIF_DEFALT_WHITE, WIF_DEFALT_THREAD_COLOUR_WHITE)
        self.Color_Table.append(whiteEntry)



class Color_Entry(object):
    def __init__(self, num, rgb):
        self.Number = num
        self.RGB = rgb
        # possible values
        # 1=40960,2304,4096
        # 2=65535,65535,65535

        # 1=0,0,0
        # 2=999,999,999
        # 3=199,0,999
        # 4=0,266,999
        # 5=0,999,999
        # 6=0,999,0
        # 7=466,999,0
        # 8=999,999,0
        # 9=999,532,0
        # 10=999,0,0
        # 11=999,0,599
        # 12=799,0,999
        # 13=517,399,999
        # COLOR TABLE

    def __str__(self):
        return str(self.Number) + " " + str(self.RGB)

    def rgb2hex(self):
        return '#%02x%02x%02x' % self.RGB

# #----------------------------------------------------------------------

class Tie_Up(object):
    '''
    '''
    def __init__(self):
        self.treadle = {}

    def get(self, config, treadle_count, max_shaft):
        # print "treadle_count", treadle_count
        for num in range(0,  treadle_count):
            strTreadle = str(num + 1)
            intTreadle = (num + 1)
            strShafts = config.get(WIF_SECTION_TIEUP, strTreadle)
            shafts = [int(n) for n in strShafts.split(',')]
            # print intTreadle, shafts
            # shafts = get_value(config, WIF_SECTION_TIEUP, str(num + 1))
            # check if the shafts are within the max_shaft
            x = True
            for i in shafts:
                if (i <= max_shaft) and (i >= 1):
                    # ok
                    # print intTreadle, i
                    pass
                else:
                    x = False
                    return None
            if (x == True):
                self.treadle[intTreadle] = shafts
        return OK

# [TIEUP]
# 1=9,8,7,3,2,1
# 2=10,6,3,2,1
# 3=11,7,6,5,3,2,1

# #----------------------------------------------------------------------

class Threading(object):
    def __init__(self):
        self.threads = {}

    def get(self, config, pattern_thread_count, shaft_count, warp_color_count, bolWarpColors):
        for num in range(0,  pattern_thread_count):
            strThread = str(num + 1)
            intThread = (num + 1)
            intShaft = config.get_int(WIF_SECTION_THREADING, strThread)
            if (CLEAR_INT == intShaft):
                intShaft = 0
            # check if shaft is within range
            if (intShaft >= 0) and (intShaft <= shaft_count):
                #OK
                pass
            else:
                print "Error shaft thread", intShaft, intThread
                return None

            if (bolWarpColors):
                intColour = config.get_int(WIF_SECTION_WARP_COLORS, strThread)
                # check if shaft is within range
                if (intColour >= 1) and (intColour <= warp_color_count):
                    #OK
                    pass
                else:
                    print "Error shaft color", intShaft, "|", intColour
                    return None
            else:
                # set default warp is black
                intColour = WIF_DEFALT_BLACK
            tmpThread = Thread(intShaft, intColour)
            self.threads[intThread] = tmpThread

        return OK

class Thread(object):
    def __init__(self, shaft, colour):
        self.Shaft = shaft
        self.Color = colour


# #----------------------------------------------------------------------

class Treadling(object):
    def __init__(self):
        self.treadles = {}

    def get(self, config, picks, treadle_count, weft_color_count, bolWarpColors):
        for num in range(0,  picks):
            strPick = str(num + 1)
            intPick = (num + 1)

            intWeftPick = config.get_int(WIF_SECTION_TREADLING, strPick)
            if (CLEAR_INT == intWeftPick):
                intWeftPick = 0
            if (intWeftPick >= 0) and (intWeftPick <= treadle_count):
                pass
            else:
                print "Error pick", intWeftPick, num
                return None

            if (bolWarpColors):
                intWeftColour = config.get_int(WIF_SECTION_WEFT_COLORS, strPick)
                if (CLEAR_INT == intWeftColour):
                    intWeftColour = 0
                if (intWeftColour >= 0) and (intWeftColour <= weft_color_count):
                    pass
                else:
                    print "Error pick num color", intWeftPick, num, intWeftColour
                    return None
            else:
                intWeftColour = WIF_DEFALT_WHITE
            tmpThread = Treadle(intWeftPick, intWeftColour)
            self.treadles[intPick] = tmpThread
        return OK

class Treadle(object):
    def __init__(self, treadle, colour):
        self.treadle = treadle
        self.Color = colour

# #----------------------------------------------------------------------

class Liftplan(object):
    def __init__(self):
        self.lift = {}

    def get(self, config, weft_thread_count, max_shaft):
        for num in range(0,  weft_thread_count):
            strLift = str(num + 1)
            intLift = (num + 1)
            strShafts = config.get(WIF_SECTION_LIFTPLAN, strLift)
            shafts = [int(n) for n in strShafts.split(',')]
            # print intLift, shafts
            # shafts = get_value(config, WIF_SECTION_TIEUP, str(num + 1))
            # check if the shafts are within the max_shaft
            x = True
            for i in shafts:
                if (i <= max_shaft) and (i >= 1):
                    # ok
                    # print intLift, i
                    pass
                else:
                    x = False
                    return None
            if (x == True):
                self.lift[intLift] = shafts
        return OK
