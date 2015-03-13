#!/usr/bin/python
import sys
import os
'''
print __file__ 
print os.path.realpath(__file__) 
print os.path.dirname(os.path.realpath(__file__))
print os.path.dirname(os.path.realpath(__file__))+'/../'
'''
#sys.path.insert(0, '/mnt/python-sessions/session6')
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/../')



import Myapp.util.mymath

print 'We are looking at 1st method of import \n'
print Myapp.util.mymath.Session5.add_it_class()

print Myapp.util.mymath.Session5.add_it_statics()

sess5obj = Myapp.util.mymath.Session5(5,10)
print sess5obj.add_it_object()
print "CLASS NAME FROM OBJECT :: "+sess5obj.__class__.__name__

print Myapp.util.mymath.Session5_sub.add_it_class()


'''  =================================================================================================== '''

from Myapp.util.mymath import Session5_sub
print "Example of selective import"
print Session5_sub.add_it_class()


''' ===================================================================================================	 '''

from Myapp.util.mymath import Session5 as main, Session5_sub as sub

print '\n\nWe are looking at 3rd method of import \n'
print main.add_it_class()

print main.add_it_statics()

sess5obj = main(5,10)
print sess5obj.add_it_object()
print "CLASS NAME FROM OBJECT :: "+sess5obj.__class__.__name__

print sub.add_it_class()
