#!/usr/bin/env python

noOfElements = int(raw_input("Enter number of entries :"))
a, b = 0,1
print a
cnt1=1
while  cnt1 <= noOfElements:
	print b
	a,b = b,a+b
	cnt1 += 1