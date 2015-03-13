#!/usr/bin/python

class base1(object):
	base1_var = 50
	"""docstring for ClassName"""
	def __init__(self):
		print "We are in the base1 class constructor"
		super(base1, self).__init__()

	def common(self):
		print "In base1 common function"

	def common_base1(self):
		print "In common_base1 function"


class base2(object):
	"""docstring for base2"""
	def __init__(self):
		print "We inside the base2 constructor"
		super(base2, self).__init__()
		
		
	def common(self):
		print "In base2 common function"

	def common_base2(self):
		print "In common_base2 function"


class derived(base2,base1):
	def __init__(self):
		print "We are inside the derived class constructor"
		super(derived, self).__init__()

	def derived_func(self):
		self.__this_is_private()
		print "Inside derived_func"

	def __this_is_private(self):
		print "This is private not accessible outside"
	


derived_obj = derived()
derived_obj.derived_func()
derived_obj.__this_is_private()
#derived_obj.common()
#print derived_obj.base1_var
#derived_obj.common_base1()
#derived_obj.common_base2()