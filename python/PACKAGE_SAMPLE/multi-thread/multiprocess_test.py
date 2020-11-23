"""
document: https://docs.python.org/2/library/multiprocessing.html

[Exchange Object between Process]:
    1.multiprocessing.Queue (simplex) : built on top of pipe
    2.multiprocessing.Pipe (duplex)  : faster than Queue
    
[Synchronization Object]:
    1.Lock() : l.acquire() l.release()
    
[Shared State]:
    1. Shared Memory: Fast,but inflexiable
        a.multiprocessing.Value
        b.multiprocessing.Array
    2. Server Process: Slow, flexiable, cross-over network. Slower than shared memory because object serialize & de-serialize
        a.multiprocessing.Manager
            i. multiprocessing.Manager.dict()
            ii.multiprocessing.Manager.list()

[pool of worker thread] 
    1.multiprocessing.Pool : not work in interactive environment
        a.pool.map ==> execut in order
        b.pool.imap_unordered ==> return iteratable object, and it is in order
        c.pool.apply_async ==> dispatch job once have job to do.
    

    
    
"""
import multiprocessing
from multiprocessing import Process
import os
from time import sleep
import numpy as np

    
def f(name):
    print name,"@",os.getpid()
    

    
def main_test_basic_process():
    p = Process(target=f, args=('bob',))
    print "p pid=", p.pid
    p1 = Process(target=f, args=('clouds',))
    print "p1 pid=", p1.pid
    
    p.start() #Start the process's activity.
    p1.start()
    print "p pid=", p.pid  #[CLS] after start() there is a pid value
    print "p1 pid=", p1.pid
    
    
    p.join() #Block the calling thread until the process whose join() method is called terminates or until the optional timeout occurs.
    p1.join()
    

def f2(x):
        sleep(np.random.rand(1))
        return (x*x , "pid=%d"%os.getpid() )
    
def main_test_pool():
    print "main pid=",os.getpid()
    
    pool = multiprocessing.Pool(processes=4)              # start 4 worker processes
    
    # print "[0, 1, 4,..., 81]"
    print "[test1]:"
    print pool.map(f2, range(10))
    
    # print same numbers in arbitrary order
    #[CLS]: return iteratable object
    print "[test2]:"
    for _ in pool.imap_unordered(f2, range(10)):
        print _,
    print ""
        
        
    # evaluate "f(20)" asynchronously
    print "[test3]:"
    res = pool.apply_async(f2, (20, ))   # runs in *only* one process
    print res.get(timeout=1)            # prints "400"

    # evaluate "os.getpid()" asynchronously
    print "[test4]:"
    res = pool.apply_async(os.getpid, ()) # runs in *only* one process
    print "res pid=",res.get(timeout=1)              # prints the PID of that process
    
    # launching multiple evaluations asynchronously *may* use more processes
    print "[test5]:"
    multiple_results = [pool.apply_async(f2, (i,)) for i in range(4)]
    print [res.get(timeout=1) for res in multiple_results]
    
    

if __name__ == '__main__':
    print "cpu count = ", multiprocessing.cpu_count()
    
    
    main_test_basic_process()
#     main_test_pool()
    
    
    
    
    
    