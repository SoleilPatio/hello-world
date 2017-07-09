import Queue as Q
"""
[CLS]:Queue module is a general queue object of python 
    the underlying object is collection.dequeue
"""



if __name__ == "__main__":
    """
    [CLS]: Normal Queue
    """
    nq = Q.Queue()
    
    nq.put(3)
    nq.put(2)
    nq.put(5)
    nq.put(1)
    nq.put(0)
    
    print "\nNormal Queue:"
    while not nq.empty():
        print nq.get(),
        
        
        
    """
    [CLS]: Priority Queue/MinHeap
    [Note]: No MaxHeap, if you want max heap, negative the key i.e 3->-3, 2->-2,...
    """
    pq = Q.PriorityQueue()
    
    pq.put(3)
    pq.put(2)
    pq.put(5)
    pq.put(1)
    pq.put(0)
    
    print "\nPriority Queue/MinHeap:"
    while not pq.empty():
        print pq.get(),
    
    
    
    """
    [CLS]: LIFO Queue/Stack
    """
    lfq = Q.LifoQueue()
    
    lfq.put(3)
    lfq.put(2)
    lfq.put(5)
    lfq.put(1)
    lfq.put(0)
    
    print "\nLIFO Queue/Stack:"
    while not lfq.empty():
        print lfq.get(),
    
    
    
    
    
    
    print "\nDone\n"