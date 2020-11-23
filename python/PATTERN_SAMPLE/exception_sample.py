import linecache
import sys
import traceback

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    traceback.print_exc(file=sys.stdout)


def _test():
    try:
        print 1/0
    except:
        PrintException()
    
if __name__ == '__main__':
    _test()
    
    
    pass