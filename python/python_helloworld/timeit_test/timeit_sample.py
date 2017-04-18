loop_count = 100

def method1():
    out_str = ''
    for num in xrange(loop_count):
        out_str += 'num'
    return out_str

def method4():
    str_list = []
    for num in xrange(loop_count):
        str_list.append('num')
    return ''.join(str_list)           
    
    
def foo():
    pass

if __name__ == "__main__":
    import timeit
    
    print timeit.timeit("method1()", setup="from __main__ import method1")
    print timeit.timeit("method4()", setup="from __main__ import method4")
    print timeit.timeit("foo()", setup="from __main__ import foo")
    
    print "Done"