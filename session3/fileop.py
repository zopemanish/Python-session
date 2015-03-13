#!/usr/bin/env python

import os
print "creating folder"
os.mkdir('newdir')
os.chdir("newdir")

print "We are in "+ os.getcwd()

fo = open("test1","w")
fo.write("2015-02-12,nfgnkjnf,dfgkjnfdkj,fdngjnfdkj\n")
fo.close()


with open("test1","a") as fo:
     fo.write("\n Yeah adding new line to file")


'''
with open("test1","r") as fo:
      file_content = fo.read()
      print file_content
'''

with open("test1","r") as fo:
	with open("test2","w") as fo1:
      for line in fo:
      	print line ,
      	fo1.write(line)

'''
fo = open("test1","r")
print "Pointer of the file ", fo.tell()
fo.seek(20,0)
file_content = fo.read()
print "\n Char at location "+file_content
fo.close()
'''
os.mkdir('newdir1')
print "test1 is file : ", os.path.isfile('test1')
print "newdir1 is file : ", os.path.isfile('newdir1')

#os.chdir("../")

#listOfFile = os.listdir('newdir1')
'''
os.remove("test1")

os.chdir("../")
os.rmdir("newdir")
'''