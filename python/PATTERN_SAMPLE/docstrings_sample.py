'''
Hotkey: Ctrl-1
'''


class Foo(object):
    def __init__(self):
        '''
        
        '''
        pass
    
    def bar(self,arg1,arg2):
        '''
        :param arg1: description
        :param arg2: description
        :type arg1: type description
        :type arg2: type description
        
        :return ret: return description
        :rtype: the return type description
        
        :var var1: Description of a variable.
        '''
        self.var1 = 1
        
        return ret
        
        pass
        




if __name__ == "__main__":
    
    print Foo.bar.__doc__
    
    
    print "\nDone!"