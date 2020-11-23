
import ConfigParser

"""
config file layout
--------------------------
[section]
option = value

"""


def WriteConfig(config_file):
    
    a_list = ["list1", 123, "list2"]
    a_dict = {
            "dict_key1": 123,
            "dict_key2": a_list
        }
    
    """
    [CLS]: default (option=value) pair
    """
    config = ConfigParser.SafeConfigParser({'bar': 'Life', 'baz': 'hard'})
    
    
    
    config.add_section("Section1")
    config.set("Section1", "key1-1", "123")
    """
    [CLS]: use str() to output string of structure
    """
    config.set("Section1", "key_a_list", str(a_list))
    
    
    config.add_section("Section2")
    config.set("Section2", "key_a_dict", str(a_dict))
    
    
    
    print "defaults->", config.defaults()
    print "sections->", config.sections()
    print "options(Section1)->", config.options("Section1")
    print "itmes(Section1)->", config.items("Section1")
    
    
    with open(config_file, 'wb') as configfile:
        config.write(configfile)



def ReadConfig(config_file):
    config = ConfigParser.SafeConfigParser()
    
    config.read(config_file)
    
    """
    [CLS]: if read twice, the latter options will overwrite previous one if duplicated
    """
    config.read("example2.cfg")
    
    ret = config.get("Section2", "key_a_dict")
    a_dict = eval(ret)
    print "readback a_dict->",a_dict
    
    
    print "defaults->", config.defaults()
    print "sections->", config.sections()
    print "options(Section1)->", config.options("Section1")
    print "itmes(Section1)->", config.items("Section1")
    
    
    

if __name__ == '__main__':
    WriteConfig('example.cfg')
    
    ReadConfig('example.cfg')
    
    
    
    
    pass