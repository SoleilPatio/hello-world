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


if __name__ == '__main__':
    import os
    print(os.getcwd())

    data = load_json_from_file("sample.json")

    print("Load data =", data)

    save_json_to_file(data, "sample-save.json")

