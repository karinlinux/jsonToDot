#! /usr/bin/env python3

import json
import sys


def extract(json_obj, pat):
    if type(json_obj) == type(dict()):
        for key in json_obj.keys():
            extract(json_obj[key], pat + key + '.')
    elif type(json_obj) == type(list()):
        for item in json_obj:
            extract(item, pat)
    else:
        print(pat.strip('.'))


if __name__ == '__main__':

    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        json_file = json.load(f)
        extract(json_file, "")
