from utils import log
from utils import ensure
from utils import isEquals

str = '0123456789'
s0 = str[0::]
log('s0', s0)
s0_1 = str[0:1:]
log('s0_1', s0_1)
# is  ==
if '#>' == '>#':
    log('true')

"""
判断 是否是 list
a = [1,2]
if 'list' in str(type(a)):
    print('1')
else:
    print('2')
a = 1
b = [1,2,3,4]
c = (1,2,3,4)
d = {‘a‘:1,‘b‘:2,‘c‘:3}
e = "abc"
if isinstance(a,int):
    print "a is int"
else:
    print "a is not int"
if isinstance(b,list):
    print "b is list"
else:
    print "b is not list"
if isinstance(c,tuple):
    print "c is tuple"
else:
    print "c is not tuple"
if isinstance(d,dict):
    print "d is dict"
else:
    print "d is not dict"
if isinstance(e,str):
    print "d is str"
else:
    print "d is not str"   

"""