class Student(object):
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age
        
    def __repr__(self):
        return "(%s,%d,%d)"%(self.name,self.score,self.age)
        


if __name__ == "__main__":
    
    data = [
            Student("Mark", 99, 10), Student("iClouds", 30, 20), Student("Sabu", 70, 15), Student("Clouds", 30, 20),
            ]
    
    
    print "Orig:", data
    
    
    """
    [CLS] in-place
    """
    data.sort( key = lambda x : x.name)
    print "Sort by name:", data
    
    """
    [CLS] new sorted list
    """
    data2 = sorted(data, key = lambda x : x.age)
    print "Sort by age:", data2
    
    
    """
    [CLS]:simpler and fast way
    :itemgetter(2) use in list object(can indexing)
    :attrgetter('age') 
    """
    from operator import itemgetter, attrgetter, methodcaller
    
    data.sort( key = attrgetter('age'))
    print "Sort by age2:", data
    
    
    data.sort( key = attrgetter('age','name'))
    print "Sort by age3 (age then name):", data
    
    
    
    
    
    print "\nDone!"