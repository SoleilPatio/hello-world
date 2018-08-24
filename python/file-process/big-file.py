
import mmap

"""
[CLS]: 
    1. only 64-bit python & os can benefit
    2. pass filename or fileno to other pprocess , don't pass mmap object directly

"""

big_file_name = r"D:\Project-D\TASKs\met_log.task\007.Sylvia_MET_Performance\Sylvia\60s\Riptide\met-20180124-125646_pf\met-20180124-125646.raw"

if __name__ == '__main__':
    
    with open(big_file_name, "r+") as f:
        # memory-map the file, size 0 means whole file
        map = mmap.mmap(f.fileno(), 0)
        
        # read content via standard file methods
        print map.readline()  # prints "Hello Python!"
        
        fsize = len(map)
        
        print "size of map =", fsize
        
        
        group_count = 10
        head_count = 1024
        offse = fsize/group_count
        
        for i in range(group_count):
            start = i*offse
            print "----------------------"
            print "%d: from %d to %d" % (i, start, start + head_count)
            map.seek(start)
            print map.readline()
#             print map[start:start+head_count]
            
        
        
        # read content via slice notation
#         print map[:]  # prints "Hello"
#         # update content using slice notation;
#         # note that new content must have same size
#         map[6:] = " world!\n"
#         # ... and read again using standard file methods
#         map.seek(0)
#         print map.readline()  # prints "Hello  world!"
#         # close the map
        map.close()
        
        
    
    pass