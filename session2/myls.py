#!/usr/bin/env python

import os
import sys
import stat

listOfFiles = os.listdir(sys.argv[1])

for i in listOfFiles:
	if os.path.isfile(i) :
		print "File "+str(i)
	else :
		print "Dir "+str(i)
