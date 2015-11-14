import os

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
        # check if its in the  list
        for fn in self.RecentWIF:
            print "File-" + fn
        if filename in self.RecentWIF:
            #print "found " + filename
            # already in the list don't duplicate
            pass
        else:
            # print "not found " + filename
            # so, add it
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
