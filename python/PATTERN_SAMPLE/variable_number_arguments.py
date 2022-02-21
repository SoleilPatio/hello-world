
def Foo(*arg):
	print ("[CLS]: *arg is a argument tuple : %s" % str(type(arg)))
	print ("arg=",arg)
	print ("")

def Bar(**kwargs):
	print ("[CLS]: **kwargs is a dict : %s" % str(type(kwargs)))
	print ("kwargs=",kwargs)
	print ("")
	
	
"""
[CLS]:" **kwargs (keyword argument)" must be the last argument
"""
def FooBar(*arg, **kwargs):
	print ("[CLS]: *arg is a argument tuple : %s" % str(type(arg)))
	print ("arg=",arg)
	print ("[CLS]: **kwargs is a dict : %s" % str(type(kwargs)))
	print ("kwargs=",kwargs)
	print ("")


def FooBarExt(arg1, arg2, *arg, **kwargs):
	print ("arg1=", arg1)
	print ("arg2=", arg2)
	print ("[CLS]: *arg is a argument tuple : %s" % str(type(arg)))
	print ("arg=",arg)
	print ("[CLS]: **kwargs is a dict : %s" % str(type(kwargs)))
	print ("kwargs=",kwargs)
	print ("")


if __name__ == "__main__":
	a_list = ["a","b","c"]
	Foo(1,2,3,"a","b","c")
	"""[CLS]: ** expand a list in un_named arguments"""
	Foo(1,2,3,*a_list)
	print ("-----------------------")
	
	a_dict = {"v1":1, "v2":2, "v3":3 }
	Bar(v1=1, v2=2, v3=3)
	"""[CLS]: ** expand a dict in named arguments"""
	Bar(**a_dict) 
	print ("-----------------------")
	
	
	FooBar(1,2,3,v1=1,v2=2,v3=3)
	FooBar(*a_list,**a_dict)
	print ("-----------------------")

	FooBarExt("arg1", "arg2", 1,2,3,v1=1,v2=2,v3=3)
	FooBarExt("arg1", "arg2", 1*a_list,**a_dict)
	print ("-----------------------")
	
	
	print ("\nDone!")
	pass