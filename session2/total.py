#! /usr/bin/python
import os

print "Current_dir: " + os.getcwd()

os.mkdir("newdir")
os.chdir("newdir")

print "New current_dir: " + os.getcwd()

fo = open("test1", "w")
fo.close()

os.rename("test1", "test2")

fo = open("test2", "w")
fo.write("Test line1.\nTest line2!!\n")
fo.close()

with open("test2", "a") as fo:
    fo.write("Test line3\n")

fo = open("test2", "r")
print "File position: ", fo.tell()

file_content = fo.read()
print "File position: ", fo.tell()

print "file_content:" + file_content

file_content = fo.read()
print "file_content:" + file_content

fo.seek(0, 0)
file_content = fo.read()
print "file_content:" + file_content

fo.close()

os.remove("test2")

os.chdir("../")
os.rmdir("newdir")




=============================================================================================================

#!/usr/bin/env python

import sys

fw = open(sys.argv[2],"wb+")

##"/mnt/python-meetup-2014/simple_text"
content = ''
with open(sys.argv[1],"rb") as fobj:
    content = fobj.readlines()

fw.writelines(content)
fw.close()

=============================================================================================================

#!/usr/bin/env python

import sys

fw = open(sys.argv[2],"wb+")

##"/mnt/python-meetup-2014/simple_text"
content = ''
with open(sys.argv[1],"rb") as fobj:
    for line in fobj:
	fw.write(line)

fw.close()

=============================================================================================================

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
