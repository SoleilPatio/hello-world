



if __name__ =="__main__":
    import collections
    
    Point = collections.namedtuple("Point",['x', 'y'])
    
    p1 = Point(1,2)
    p2 = Point(3,4)
    
    """
    [CLS]:namedtuple is immutable. Used this to defined constant
    """
    p2.x = 100
    
    print p1
    print p2
    
    
    
    print "Done"