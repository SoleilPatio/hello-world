"""
Sample 1: basic decorate 
"""

def my_decorate(func):
    
    def wraper(*args, **kwargs):
        print "Begin decorate for \"%s\"" %func.__name__
        print "\t",
        ret = func(*args, **kwargs)
        print "End decorate"
        return ret
    
    return wraper
        

"""
[CLS]: "@my_decorate" do the following thing:
    
    basic_func = my_decorate(basic_func)
              = my_decorate.wraper
              
    basic_func( msg ) = my_decorate.wraper(msg)
     
"""
@my_decorate
def basic_func( msg ):
    print msg
    



"""
Sample 2: decorate with parameters 
"""

"""
[CLS]: decorator can have parameters
"""   
def my_decorate_with_options(deco_option):
    print "deco option:", deco_option
    def decorator(func):
        def wraper(*args, **kwargs):
            print "Begin decorate for \"%s\"" %func.__name__
            print "I have deco option:", deco_option
            print "\t",
            ret = func(*args, **kwargs)
            print "End decorate"
            return ret
        
        return wraper
    return decorator

@my_decorate_with_options("this is decorate option")
def basic_func2( msg ):
    print msg


"""
Sample 3: class decorate
"""
class my_class_decorate(object):
    def __init__(self, func):
        self._func = func
        
    def __call__(self, *args, **kwargs):
        print "Begin class decorate for \"%s\"" %self._func.__name__
        print "\t",
        ret = self._func(*args, **kwargs)
        print "End decorate"
        return ret
        


@my_class_decorate
def basic_func3( msg ):
    print msg


"""
Sample 4: class decorate with parameters
"""
class my_class_decorate_with_options(object):
    def __init__(self, flag):
        self._flag = flag
        
    def __call__(self, origin_func):
        
        def wrapper(*args, **kwargs):
            print "Begin class decorate for \"%s\",option=%s" % (origin_func.__name__, self._flag)
            print "\t",
            ret = origin_func(*args, **kwargs)
            print "End decorate"
            return ret
        
        return wrapper
        


@my_class_decorate_with_options("DECO OPTIONS")
def basic_func4( msg ):
    print msg



if __name__ == '__main__':
    basic_func("I am original message!")
    basic_func2("II am original message!")
    basic_func3("III am decorated by Class!")
    basic_func4("IV am decorated by Class with parameters!")
    
    
    
    pass