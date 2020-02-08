# -*- coding: utf-8 -*-
#[CLS]: "coding utf-8" 要在前兩行，py檔案裏面才可以出現 Non-ASCII character


#[CLS]:pip install chardet 
import chardet


if __name__ == '__main__':
    
    ret = chardet.detect(u"此字符集支持部分於歐洲使用的語言".encode("big5"))
    
    """
    output:
    {'confidence': 0.99, 'language': 'Chinese', 'encoding': 'Big5'}
    """
    print ret
    