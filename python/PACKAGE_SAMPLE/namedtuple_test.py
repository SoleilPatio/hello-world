



if __name__ =="__main__":
    import collections
    
    """
    [CLS]:
        1. Point is a new-created class name
        2. "Point_data_type_name" is the data type name
    """
    Point = collections.namedtuple("Point_data_type_name",['x', 'y'])
    
    p1 = Point(1,2)
    p2 = Point(3,4)
    p3 = Point("this is x","this is y")
    
    """
    [CLS]:namedtuple is immutable. Used this to defined constant
         [NOTE!!!!]: ONLY FOR CONSTANT
    """
    
    print p1.x, p1.y
    print p1[0], p1[1]
    print "type=",type(p1)
    print p2
    print p3
    
    
    print "Done"