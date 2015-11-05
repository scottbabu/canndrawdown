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
        # self.wif = {}
        self.wif = {"Section":{"Key":"Value"}}
        # self.wif["Section"]["Key"] = "Value"

    def Read(self, wif_name):
        # open file read each line into a list then close file
        #
        line_num = 0
        current_section = ""
        # print(self.wif)

        fh = open(wif_name, "r")
        # strip off carrage return and line feed
        for cur_line in fh.read().split('\r\n'):
            # check for blank line
            if bool(cur_line):
                # parse into wif structure
                # section , comment, or key/value
                # print(cur_line)
                if (cur_line[0] == ";"):
                    # comment
                    # self.wif.update({WIF_SECTION_COMMENT:{line_num:cur_line}})
                    # if its not there create it
                    if WIF_SECTION_COMMENT in self.wif.keys():
                        self.wif[WIF_SECTION_COMMENT][line_num] = cur_line
                    else:
                        # self.wif = {WIF_SECTION_COMMENT:{line_num:cur_line}}
                        self.wif.update({WIF_SECTION_COMMENT:{line_num:cur_line}})
                elif (cur_line[0] == "["):
                    # section
                    # remove braces and change from the current cAsE to 'Title Case'
                    current_section = cur_line.replace("[","").replace("]","").title()
                    self.wif.update({current_section:{line_num:line_num}})
                else:
                    # key/value and everything else
                    key, value = cur_line.split("=")
                    self.wif[current_section][key.title()] = value
                    # self.wif.update({current_section:{key.title():value}})

                line_num = line_num + 1
            fh.close()

    # def get(self, section, key):
    #     '''
    #     from the list self.wif get the value from section key
    #     '''

wif = WIF()
wif.Read("9041.wif")
# print wif.wif[29].Line_Num, wif.wif[29].Section, wif.wif[29].Key, wif.wif[29].Value
# print(wif.wif)
print(wif.wif.keys())
for k, v in wif.wif.items():
    print k
    for key, val in v.items():
        print key, val
