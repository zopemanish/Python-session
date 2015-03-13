#!/usr/bin/env python

noOfElements = int(raw_input("Enter number of entries :"))
'''
a = 0
b = 1
print a
for i in range(1,noOfElements):
	print b
	b,a = a+b,b
'''

a = 0
b = 1
c = b
print a
for i in range(1,noOfElements):
	print c
	c = a + b
	a = b
	b = c