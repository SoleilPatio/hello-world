



if __name__ =="__main__":
    import collections
    
    Point = collections.namedtuple("Point",['x', 'y'])
    
    p1 = Point(1,2)
    p2 = Point(3,4)
    p3 = Point("this is x","this is y")
    
    """
    [CLS]:namedtuple is immutable. Used this to defined constant
         [NOTE!!!!]: ONLY FOR CONSTANT
    """
    
    print p1
    print p2
    print p3
    
    
    print "Done"