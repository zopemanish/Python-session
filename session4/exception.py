#!/usr/bin/python

# d = {'k':'v'}
# print d['k']

# print d['k2']

# if 1:
# print "somthing"

# print 2/0

# class MyError(Exception):
# 		pass

# try:
# 	print1
# 	# divisor = 0
# 	# if divisor == 0:
# 	# 	raise MyError
# except MyError:
# 	print "divisor can not be 0"

class MyException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

try:
	print1
except:
	raise MyException("Divide by blah blah")