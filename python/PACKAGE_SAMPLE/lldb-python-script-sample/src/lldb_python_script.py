"""
script print os.getcwd()

command script import ./project/hello-world/python/lldb-python-script-sample/src/lldb_python_script.py
command script import /proj/mtk02679/project/hello-world/python/lldb-python-script-sample/src/lldb_python_script.py
"""
import lldb
import linecache
import sys
import traceback
import commands
import argparse

"""
[CLS] work around for argparse in embedded python 
"""
import sys
if not hasattr(sys, 'argv'):
    sys.argv  = ['']




print "hello!LLDB"

#CMEMO: fix this shity bug
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    traceback.print_exc(file=sys.stdout)

  
def ls(debugger, command, result, internal_dict):
    try:
        print "[%s()]:"%("ls")
        print "\tcommand: ",command , type(command)
        print "\tresult: ",result , type(result)
        print "\tinternal_dict: ",type(internal_dict)
        
        parser = argparse.ArgumentParser()
        parser.add_argument("-foo", help="info for foo", default="default value")
        parser.add_argument("-bar", help="info for bar", default="default value")
        parser.add_argument("file", nargs='?', default="default value")
        args = parser.parse_args(command.split())
    
        print "\targs = ", args
        
        
        print >>result, (commands.getoutput('/bin/ls %s' % command))
        
        print "[%s()]:Done\n"%("ls")
        
    except:
        PrintException()
        


def __lldb_init_module(debugger, internal_dict):
    try:
        print "[%s()]:"%("__lldb_init_module") 
        print "\tdebugger:", debugger
        print "\tdebugger:", lldb.debugger
        print "\ttarget:", lldb.target
        print "\tprocess:", lldb.process
        print "\tthread:", lldb.thread
        print "\tframe:", lldb.frame
        
        
        debugger.HandleCommand('command script add -f lldb_python_script.ls  ls')
        
    except:
        PrintException()
        
    print "[%s()]:Done\n"%("__lldb_init_module")
        
    
        

def other_func():
    print "other_func"
    
if __name__ == "__main__":
    print "main"