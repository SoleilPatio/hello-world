
def Foo(*arg):
	print "[CLS]: *arg is a argument tuple : %s" % str(type(arg))
	print "arg=",arg

def Bar(**kwargs):
	print "[CLS]: **kwargs is a dict : %s" % str(type(kwargs))
	print "kwargs=",kwargs
	
	
"""
[CLS]:" **kwargs" must be the last argument
"""
def FooBar(*arg, **kwargs):
	print "[CLS]: *arg is a argument tuple : %s" % str(type(arg))
	print "arg=",arg
	print "[CLS]: **kwargs is a dict : %s" % str(type(kwargs))
	print "kwargs=",kwargs


if __name__ == "__main__":
	Foo(1,2,3,"a","b","c")
	Bar(v1=1, v2=2, v3=3, v4="a", v5="b", v6_6="c")
	FooBar(1,2,3,v1=1,v2=2,v3=3)
	
	
	print "\nDone!"
	pass