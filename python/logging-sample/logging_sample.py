import logging

"""
Level    When it's used

DEBUG    Detailed information, typically of interest only when diagnosing problems.
INFO    Confirmation that things are working as expected.
WARNING    An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
ERROR    Due to a more serious problem, the software has not been able to perform some function.
CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
"""

"""
Attribute name    Format    Description
args    You shouldn't need to format this yourself.    The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).
asctime    %(asctime)s    Human-readable time when the LogRecord was created. By default this is of the form '2003-07-08 16:49:45,896' (the numbers after the comma are millisecond portion of the time).
created    %(created)f    Time when the LogRecord was created (as returned by time.time()).
exc_info    You shouldn't need to format this yourself.    Exception tuple (sys.exc_info) or, if no exception has occurred, None.
filename    %(filename)s    Filename portion of pathname.
funcName    %(funcName)s    Name of function containing the logging call.
levelname    %(levelname)s    Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
levelno    %(levelno)s    Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
lineno    %(lineno)d    Source line number where the logging call was issued (if available).
module    %(module)s    Module (name portion of filename).
msecs    %(msecs)d    Millisecond portion of the time when the LogRecord was created.
message    %(message)s    The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
msg    You shouldn't need to format this yourself.    The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).
name    %(name)s    Name of the logger used to log the call.
pathname    %(pathname)s    Full pathname of the source file where the logging call was issued (if available).
process    %(process)d    Process ID (if available).
processName    %(processName)s    Process name (if available).
relativeCreated    %(relativeCreated)d    Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
thread    %(thread)d    Thread ID (if available).
threadName    %(threadName)s    Thread name (if available).
"""

"""
[CLS]:
    logging ==> module-level function
    logger ===> logger object 
"""
def log_to_console():
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    

def log_to_file():
    """
    [CLS] basicConfig() must be called before any other function
          if run logging.info/debug before basicConfig, no log file created
    """
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

def log_format():
    """
    [CLS] basicConfig() must be called before any other function
          if run logging.info/debug before basicConfig, no log file created
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(name)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')


"""
[CLS]: can be hierarchical  if logger name is like hfoo.bar.baz
"""
def logger_test():
    print "__name__ = ", __name__
    logger = logging.getLogger(__name__)
    print "%s effective level = %d"% ( __name__, logger.getEffectiveLevel() )
    logger.setLevel(logging.CRITICAL)
    print "%s effective level = %d"% ( __name__, logger.getEffectiveLevel() )
    logger.info("I am logger")
    
    
    # create logger
    logger2 = logging.getLogger('logger2')
    print "%s effective level = %d"% ( 'logger2', logger2.getEffectiveLevel() )
    logger2.setLevel(logging.CRITICAL)
    print "%s effective level = %d"% ( 'logger2', logger2.getEffectiveLevel() )
    logger2.info("I am logger2")
    
    
    
def logger_handle():
    # create formatter
    formatter = logging.Formatter('[%(levelname)s][%(name)s]:%(message)s')
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.NOTSET) #noset means all record will be processed by handler

    # add formatter to ch
    ch.setFormatter(formatter)
    
    #get logger
    logger = logging.getLogger("LOGGERHDL")
    logger.setLevel(logging.DEBUG) #if is NOSET, level will use logger.parent's level

    # add ch to logger
    logger.addHandler(ch)
    
    
    #Start logging
    logger.info("logger_handle,logger_handle,logger_handle")
    
    
    
    
    

if __name__ == '__main__':
    """
    [CLS] get log level
    """
    
#     log_to_console()
#     log_to_file()
    log_format()
    
    
    logger_test()
    
    logger_handle()
    
    print "loglevel = ", getattr(logging, "loglevel", None)
    
    pass