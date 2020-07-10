
"""
subprocess
os.system
os.spawn
os.popen --abandon
popen2.* --abandon
commands.* --abandon in 3.x
"""

"""
1. commands spaws a shell which does the glob expansion.  subprocess doesn't spawn a shell unless you pass shell = True.
2. Subprocess gives you much more control over what's going on.
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


def Run_CMD( command_line, feature_context ):
    #........................................................
    # Console encoding issue
    #........................................................
    default_console_encoding="big5" #for most .bat output

    #........................................................
    # Execute command line
    #........................................................
    cmd_str = command_line
    # print("[CMD] %s"%cmd_str)
    logging.info("[CMD] %s"%cmd_str)
    output = subprocess.Popen( cmd_str, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = output.communicate()

    #........................................................
    # (Option) Auto Detect Console encoding (not 100%)
    #........................................................
    # import chardet
    # encoding = chardet.detect(std_out)
    # print("encoding=", encoding)
    # default_console_encoding = encoding["encoding"]

    feature_context["stdout"] = std_out.decode(encoding=default_console_encoding).splitlines() #it's byte object
    feature_context["stderr"] = std_err.decode(encoding=default_console_encoding).splitlines() #it's byte object

    msg = "[CMD stdout] out=[\n%s\n]"%(std_out.decode(encoding=default_console_encoding)) #std_err is byte type
    logging.info(msg)

    if output.returncode != 0:
        # msg = "[CMD stderr] ret=%s cmd=%s err=[\n%s\n]"%(output.returncode, cmd_str, std_err.decode()) #std_err is byte type
        msg = "[CMD stderr] ret=%s err=[\n%s\n]"%(output.returncode, std_err.decode(encoding=default_console_encoding)) #std_err is byte type
        logging.error(msg)
        print("[ERROR] %s"%msg)
    return output.returncode


if __name__ == '__main__':
    
    commands_test()
    
    subprocess_test()
    
    subprocess_pipe()
    
    
    pass
