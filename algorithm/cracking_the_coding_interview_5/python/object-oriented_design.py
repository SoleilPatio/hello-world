"""
Singleton
"""

class Singleton(object):
    instance = None
    
    def __init__(self,a):
        self.a = a
    
    def getInstance(self):
        if Singleton.instance == None:
            Singleton.instance = Singleton(99)
        return Singleton.instance
    
    
    
            
def main_singleton_test():
    obj1 = Singleton(1)
    print obj1.a
    
    sig1 = obj1.getInstance()
    print sig1.a
    
    
    obj2 = Singleton(2)
    print obj2.a
    
    sig2 = obj2.getInstance()
    print sig2.a
    



if __name__ == "__main__":
    main_singleton_test()
    
    print "Done"
    
    
    