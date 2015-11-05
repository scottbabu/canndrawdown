#!/usr/bin/env python

import sys
from WIF import *

if (len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    # filename = 'data/susantowels.wif'
    filename = 'data/34143-s.wif'


wif = Weaving_Info_File()
wif.read_wif(filename)
print wif.Version, wif.Developers
print wif.contents
print wif.weaving
print wif.warp
print wif.weft
for thr in wif.threading.threads:
    print thr, wif.threading.threads[thr].Shaft, wif.threading.threads[thr].Color
print wif.color_palette.Color_Table
