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
    
+-----------+----------------------------------------+-----------------+-------------------+
| function  |                  Note                  |       ^$        | re.MULTILINE/re.M |
+-----------+----------------------------------------+-----------------+-------------------+
| match()   | search from begin of str               |                 |                   |
| search()  | search from anywhere in str            | ^:begin of str  | ^:begin of line   |
| findall() | search many times from anywhere in str | same as search? | same as search?   |
| sub()     | same as find all and replace           | same as search? | flags=re.M        |
+-----------+----------------------------------------+-----------------+-------------------+


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
    
    
def RE_Replace():
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
    
    
    
def RE_KeyValuePairToDictionary():
    in_string = "key1='this is key1', key2='ThisIsKey2', key3='key3 has no comma'"
    
    """
    [CLS]:(?= )   ==> means "matched but not be included"
    """
    patternObj = re.compile(r"\s*([^=,]+)\s*=\s*([^=]+)(?=,|$)", re.M)
    
    print patternObj.findall(in_string)
    new_dict = dict( patternObj.findall(in_string) )
    print new_dict
    
    
    
"""
Repeat Pattern
"""    
def RE_FindAll():
    s1 = "irq=2 name=arch_timer"
    s2 = "hw_module=4, imgo_en=1, rrzo_en=4, imgo_bpp=0, rrzo_bpp=0, imgo_xsize=3339, imgo_ysize=0, rrzo_xsize=3599, rrzo_ysize=1079, rrz_src_w=2672, rrz_src_h=2008, rrz_dst_w=1920, rrz_dst_h=1080, rrz_hori_step=45608, rrz_vert_step=45614, DISP_OVL0_2L__OVL_L1_CON=12544"
    
    re.findall(r"\w+=\w+", s2)     

    
    
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
    RE_Sample()
    RE_Replace()
    RE_KeyValuePairToDictionary()
#     RE_PatternTest()
    
