
import thread
import time
import os
import numpy as np
from time import sleep

global_var = "null"


# Define a function for the thread
def print_time( threadName, delay):
    count = 20
    
    while count:
        print "%s: pid:%d (%s)" % ( threadName,  os.getpid(), global_var )
        count-=1
        sleep(np.random.rand(1))



if __name__ == '__main__':
    print "main pid=",os.getpid()
    
    # Create two threads as follows
    try:
        thread.start_new_thread( print_time, ("Thread-1", 1, ) )
        thread.start_new_thread( print_time, ("Thread-2", 1, ) )
    except:
        print "Error: unable to start thread"
    
    while 1:
        global_var = time.ctime(time.time())
        pass
   
    print "Done!"
    pass