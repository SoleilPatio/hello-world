# -*- coding: utf-8 -*-
import chardet


if __name__ == '__main__':
    
    ret = chardet.detect(u"此字符集支持部分於歐洲使用的語言".encode("big5"))
    
    """
    output:
    {'confidence': 0.99, 'language': 'Chinese', 'encoding': 'Big5'}
    """
    print ret
    