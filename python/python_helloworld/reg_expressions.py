'''
'''
import re

def RE_Sample():
    """
    re.I    Performs case-insensitive matching.
    re.L    Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior (\b and \B).
    re.M    Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
    re.S    Makes a period (dot) match any character, including a newline.
    re.U    Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
    re.X    Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.
    """
    
    line = "Cats are smarter than dogs"
    
    """
    [CLS]:Part 1:
    [CLS]:match() ==> check from beginning
    """
    print "[re.match()]:"
    matchObj = re.match( r"(.*) are (.*?) .*", line, re.M|re.I)
    if matchObj:
        """[CLS]: return all matching subgroups as touple"""  
        print "groups():",matchObj.groups()
        print "group():",matchObj.group()
        print "group(0):",matchObj.group(0)
        print "group(1):",matchObj.group(1)
        print "group(2):",matchObj.group(2)
    else:
        print "No match"
        
        
        
    """
     [CLS]:Part 2:
    [CLS]:search() ==> check anywhere (Perl default)
    """   
    print "[re.search()]:"
    matchObj = re.search( r"(.*) are (.*?) .*", line, re.M|re.I)
    if matchObj:
        """[CLS]: return all matching subgroups as touple"""  
        print "groups():",matchObj.groups()
        print "group():",matchObj.group()
        print "group(0):",matchObj.group(0)
        print "group(1):",matchObj.group(1)
        print "group(2):",matchObj.group(2)
    else:
        print "No match"


    """
     [CLS]:Part 3:
    [CLS]:compile() ==> increase performance
    """
    patternObj = re.compile(r"(.*) are (.*?) .*", re.M|re.I)
    
    print "[re.compile match()]:"
    matchObj = patternObj.match(line)
    if matchObj:
        """[CLS]: return all matching subgroups as touple"""  
        print "groups():",matchObj.groups()
        print "group():",matchObj.group()
        print "group(0):",matchObj.group(0)
        print "group(1):",matchObj.group(1)
        print "group(2):",matchObj.group(2)
    else:
        print "No match"
        
    print "[re.compile search()]:"
    matchObj = patternObj.search(line)
    if matchObj:
        """[CLS]: return all matching subgroups as touple"""  
        print "groups():",matchObj.groups()
        print "group():",matchObj.group()
        print "group(0):",matchObj.group(0)
        print "group(1):",matchObj.group(1)
        print "group(2):",matchObj.group(2)
    else:
        print "No match"
    
    
        
        
    """
     [CLS]:Part 4:
    [CLS]:replace() will return a new string
    """
    print "[re.sub()]:"
    phone = "2004-959-559 # This is Phone Number"
    
    # Delete Python-style comments
    """
    [CLS]:Phone Num :  2004-959-559
    """
    num = re.sub(r'#.*$', "", phone)
    print "Phone Num : ", num
    
    # Remove anything other than digits
    """
    [CLS]:Phone Num :  2004959559
    """
    num = re.sub(r'\D', "", phone)    
    print "Phone Num : ", num
    
    
def RE_PatternTest():
    lines = [
             
             ]
    
    pattern = re.compile("\s*([^\s]*)-([^\s-]*)\s+([^\s]*)\s+([^\s]*):\s*(.*):\s*(.*)")
    
    for line in lines:
        print "----------------------------"
        matchobj = pattern.search(line)
        if matchobj:
            print "len=", len(matchobj.groups())
            for g in matchobj.groups():
                print g
                
                
            
    
    
    

if __name__ == '__main__':
#     RE_Sample()
    RE_PatternTest()
    
