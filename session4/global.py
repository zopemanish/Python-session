#!/usr/bin/python

number = 50

def print_number():
	global number
	number = 20
	print number

print_number()
print number
