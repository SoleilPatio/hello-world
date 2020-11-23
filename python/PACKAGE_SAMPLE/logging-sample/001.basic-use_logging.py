#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# [Reference Material]
# Document: https://docs.python.org/3/library/logging.html
# HOWTO: https://docs.python.org/3/howto/logging.html
# Cookbook: https://docs.python.org/3/howto/logging-cookbook.html
# Flow Chart: https://docs.python.org/3/_images/logging_flow.png


# [Main Classes]
# Loggers expose the interface that application code directly uses.
# Handlers send the log records (created by loggers) to the appropriate destination.
# Filters provide a finer grained facility for determining which log records to output.
# Formatters specify the layout of log records in the final output.


# [Debug Level]
# DEBUG   Detailed information, typically of interest only when diagnosing problems.
# INFO    Confirmation that things are working as expected.
# WARNING An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR   Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL    A serious error, indicating that the program itself may be unable to continue running.



if __name__ == '__main__':
    import logging

    
    #[CLS] logging.basicConfig 只能呼叫設定一次，以後就沒用了
    #      The call to basicConfig() should come before any calls to debug(), info() etc. 
    #[CLS] log level
    logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(level=logging.WARNING)  
    #[CLS] log to file
    # logging.basicConfig(filename='example.log',level=logging.DEBUG)  #[CLS] log file append
    # logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)  #[CLS] log file overwrite
    #[CLS] log format
    # logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG) 
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


    #[CLS] 直接使用logging來log (root logger隱藏在其中)
    count = 1
    logging.debug('[%d] - debug message' % count)
    logging.info('[%d] - info message' % count)
    logging.warning('[%d] - warning message' % count)  
    logging.error('[%d] - error message' % count)
    logging.critical('[%d] - critical message' % count)


    count = 2
    logging.basicConfig(filename='example.log',level=logging.WARNING) #[CLS] basicConfig()只能呼叫一次, 之後呼叫設定沒用了
    logging.debug('[%d] - debug message' % count)
    logging.info('[%d] - info message' % count)
    logging.warning('[%d] - warning message' % count)  
    logging.error('[%d] - error message' % count)
    logging.critical('[%d] - critical message' % count)

    
    #[CLS] 直接使用logging的logger,就是root logger
    count = 3
    root_logger = logging.getLogger()           #[CLS] getLogger() 不加參數抓出logging預設的"root" logger物件
    root_logger.setLevel(logging.WARNING)       #[CLS] 要改變要抓logger物件出來設定
    root_logger.debug('[%d] - debug message' % count)
    root_logger.info('[%d] - info message' % count)
    root_logger.warning('[%d] - warning message' % count)  
    root_logger.error('[%d] - error message' % count)
    root_logger.critical('[%d] - critical message' % count)

