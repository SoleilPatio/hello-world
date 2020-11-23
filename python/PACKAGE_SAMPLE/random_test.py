from random import SystemRandom

if __name__ == '__main__':
    cryptogen = SystemRandom()
    a= [cryptogen.randrange(3) for i in range(20)]
    
    COUNT = 1000000
    RANGE = 100
    
    count = 0
    more = 0
    while True:
        n = cryptogen.randrange(RANGE)
        bool = n >= (RANGE/2)
        count += 1
        if bool:
            more += 1
            
        if count == COUNT:
            ratio = float(more)/COUNT
            print ratio
            count = 0
            more = 0
            
            
        
        
        
    
    pass