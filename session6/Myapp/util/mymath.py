#!/usr/bin/python

class Session5(object):
	a = 5
	b = 10
	"""docstring Session5"""
	def __init__(self, c, d):
		super(Session5, self).__init__()
		self.c = c
		self.d = d

	@classmethod
	def add_it_class(cls):
		''' When called on the subclass it will return the sub class '''
		print str(cls.__name__)
		return cls.a+cls.b

	@staticmethod	
	def add_it_statics():
		return Session5.a+Session5.b

	def add_it_object(self):
		return self.c+self.d


class Session5_sub(Session5):
	"""docstring for Session5_sub"""
	a = 20
	b = 25
	def __init__(self, ):
		super(Session5_sub, self).__init__()
