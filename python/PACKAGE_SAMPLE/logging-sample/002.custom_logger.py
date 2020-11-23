#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import logging

#[CLS] 結論:
#       1.在所有module都直接用logging直接打印
#       2.統一由App層來設定 debug level
#       3.統一由App層來決定加掛的handler


class MyHandler(logging.StreamHandler):
    def emit(self, record):
        print("----------------------------------------")
        print("format_msg=", self.format(record))
        print("message=", record.message)
        print("module=", record.module)
        print("filename=", record.filename)
        print("funcName=", record.funcName)
        print("lineno=", record.lineno)
        print("levelname=", record.levelname)
        print("name=", record.name)
        print("pathname=", record.pathname)
        print("processName=", record.processName)
        print("process=", record.process)
        print("threadName=", record.threadName)
        print("thread=", record.thread)

        


if __name__ == '__main__':
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




    #[CLS] 直接使用logging的logger,就是root logger
    count = 1
    logging.debug('[%d] - debug message' % count)
    logging.info('[%d] - info message' % count)
    logging.warning('[%d] - warning message' % count)  
    logging.error('[%d] - error message' % count)
    logging.critical('[%d] - critical message' % count)


    
    #[CLS] 抓出root logger,並將MyHandler"附加"上去,不影響原來的stand out log
    count = 2
    my_handler = MyHandler()
    root_logger = logging.getLogger()           #[CLS] getLogger() 不加參數抓出logging預設的"root" logger物件
    root_logger.addHandler(my_handler)          #[CLS] 對 root logger 加上自己的handler


    logging.debug('[%d] - debug message' % count)   #[CLS]還是用logging來打印
    logging.info('[%d] - info message' % count)
    logging.warning('[%d] - warning message' % count)  
    logging.error('[%d] - error message' % count)
    logging.critical('[%d] - critical message' % count)

