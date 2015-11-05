import os
import string
from resource import *

class WIFLine(object):
    def __init__(self):
        self.Line_Num = 0
        self.Section = "" # [], comment,
        self.Key = ""
        self.Value = ""

# def get_value(config, section, key):
#     try:
#         sv = config.get(section,key)
#         return sv
#     # except ConfigParser.NoSectionError:
#     #     return CLEAR_INT
#     # except ConfigParser.NoOptionError:
#     #     return CLEAR_INT

class WIF(object):
    '''
    '''
    def __init__(self):
        self.wif = []

    def Read(self, wif_name):
        # open file read each line into a list then close file
        #
        line_num = 0
        current_section = ""

        fh = open(wif_name, "r")
        for cur_line in fh.read().split('\r\n'):
            cur_wif = WIFLine()
            # check for blank line
            # print cur_line, len(cur_line), bool(cur_line)
            if bool(cur_line):
                # create wif line instance
                # strip off carrage return and line feed
                # cur_line = line.rstrip('\r\n')
                # set line number on current instance
                cur_wif.Line_Num = line_num
                # parse into wif structure
                # section , comment, or key/value
                if (cur_line[0] == ";"):
                    # comment
                    cur_wif.Section = WIF_SECTION_COMMENT
                    cur_wif.Key = WIF_SECTION_COMMENT
                    cur_wif.Value = cur_line
                elif (cur_line[0] == "["):
                    # section
                    # remove braces and change from the current cAsE to 'Title Case'
                    current_section = cur_line.replace("[","").replace("]","").title()
                    cur_wif.Section = current_section
                    cur_wif.Key = current_section
                    cur_wif.Value = current_section
                else:
                    # key/value and everything else
                    cur_wif.Section = current_section
                    key, value = cur_line.split("=")
                    cur_wif.Key = key.title()
                    cur_wif.Value = value

                self.wif.append(cur_wif)
                line_num = line_num + 1
            fh.close()

    # def get(self, section, key):
    #     '''
    #     from the list self.wif get the value from section key
    #     '''

wif = WIF()
wif.Read("9041.wif")
print wif.wif[29].Line_Num, wif.wif[29].Section, wif.wif[29].Key, wif.wif[29].Value
