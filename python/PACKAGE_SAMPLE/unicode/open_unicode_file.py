# -*- coding: utf-8 -*-
import os


if __name__ == '__main__':

    """
    [CLS]:listdir return list of filenames in unicode string
    """
    filelist = os.listdir(u"sample_file\\")
    print filelist
    for file in filelist:
        print type(file), file
        
        
    """
    [CLS]:pass a unicode string u"...." to open()
          ?). But the content line is ascii
    """
    filename = u"sample_file\\简体双语.Unbreakable.Kimmy.Schmidt.S02E01.720p.WEBRip.x264-FLEET.电波字幕组.ass" 
    
    with open(filename) as in_file:
        for line in in_file:
            print type(line),line
    
    pass
