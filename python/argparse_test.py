import argparse

__version_info__ = ('2013','03','14')
__version__ = '-'.join(__version_info__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-foo", help="info for foo", default="default value")
    parser.add_argument("-bar", help="info for bar", default="default value", required=True)
    parser.add_argument("-boolean",  action="store_true", help="increase output verbosity")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    
    """
    [CLS]: a positional argument (no -- option in front of the name) , always requires
    """
    parser.add_argument("square", type=int, help="display a square of a given number")
    #"--verbose",
    """
    [CLS]: if argements are illegal, this "parse_args" will show help and exit program
    """
    args = parser.parse_args()

    print "args = ", args
    
    
    print "Done"