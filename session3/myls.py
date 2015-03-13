#!/usr/bin/env python
import os
import sys

listOfFiles = os.listdir(sys.argv[1])

for file1 in listOfFiles:
   if os.path.isfile(file1):
        print file1 + " - file"
   else:
        print file1+ " - dir" 
