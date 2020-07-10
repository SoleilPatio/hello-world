# -*- coding: utf-8 -*-
from __future__ import print_function
import json


def load_json_from_file(json_file_name):
    with open(json_file_name) as infile:
        data = json.load(infile)
    return data


def save_json_to_file(data, json_file_name):
    with open(json_file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def StrObj(obj):
    #Python 2
    # return json.dumps(obj, indent=4 , sort_keys=True).decode('unicode-escape').encode('utf-8')
    #Python 3
    return json.dumps(obj, indent=4 , sort_keys=True, ensure_ascii=False ) #ensure_ascii=false for non-ascii character

def SaveToJsonFile(obj, json_file_name):
    pathlib.Path(json_file_name).parent.mkdir(parents=True, exist_ok=True)
    with codecs.open(json_file_name, 'w' , encoding='utf-8') as outfile: #Good for Chinese characters
        # outfile.write(StrObj(obj)) #Good
        json.dump(obj, outfile, indent=4 , ensure_ascii=False, sort_keys=True) #Good
        

if __name__ == '__main__':
    import os
    print(os.getcwd())

    data = load_json_from_file("sample.json")

    print("Load data =", data)

    save_json_to_file(data, "sample-save.json")

