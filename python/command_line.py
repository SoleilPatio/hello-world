
"""
subprocess
os.system
os.spawn
os.popen --abandon
popen2.* --abandon
commands.* --abandon in 3.x
"""


def commands_test():
    import commands
    
    ret = commands.getoutput('/bin/ls -l')
    
    print ret
    
def subprocess_test():
    import subprocess
    
    """
    [CLS]: BLOCK. wait for command finish
    """
    subprocess.call(["ls", "-l", "-t"])
    subprocess.call("ls -l -t", shell = True)
    
    """
    [CLS]: BLOCK. check return code if is 0, if not exception
    """
    if subprocess.check_call(['ls']) == 0:
        print('Command Success Execute')
    else:
        print('Oops, something error')
    
    
    """
    [CLS]: BLOCK. return output, and check return code if is 0, if not exception
    """
    output = subprocess.check_output(["ls", "-l", "-t"])
    print output
    
    
    
def subprocess_pipe():
    
    from subprocess import Popen, PIPE
    """
    [CLS]:can handle process's input,output,and stderr
    """
    p = Popen(['ls',".","Not_Exist_File"], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    stdout, stderr = p.communicate(input='aweimeow\n')
    print "stdout=",stdout
    print "stderr=",stderr



if __name__ == '__main__':
    
    commands_test()
    
    subprocess_test()
    
    subprocess_pipe()
    
    
    pass