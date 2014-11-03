#!env python

# -*- coding:utf-8 -*-

"""
Comment here
"""

__author__ = 'qiuxiafei'

import sys
import argparse
import json


def parse_query(query_str):
    res = []
    is_digit = False
    item = ''
    for i in query_str + '.':
        if i == '.' or i == ']':
            if not is_digit:
                if item:
                    res.append(item)
            elif is_digit and item.isdigit():
                res.append(int(item))
            else:
                raise Exception('Digits is expected in [], but %s is provided.' % item)
            item = ''
            is_digit = False
        elif i == '[':
            if item:
                res.append(item)
            item = ''
            is_digit = True
        else:
            item += i
    return res


def do_query(json_str, query_str):
    data = json.loads(json_str)
    query = parse_query(query_str)
    res = data
    for i in query:
        if not res:
            break
        if isinstance(i, int):
            if isinstance(res, list):
                res = res[i]
            else:
                raise Exception('Digit should be with list')
        elif isinstance(i, str):
            if isinstance(res, dict):
                res = res.get(i)
            else:
                raise Exception('String should be with map')
        else:
            raise Exception('Invalid query item [%s] of %s' % (i, type(i)))
    json.dump(res, sys.stdout)
    print


def get_option_parser():
    p = argparse.ArgumentParser(description="Parse argument of query json.")
    p.add_argument('-e', metavar='query_expression', dest='expr', required=True)
    p.add_argument('-j', metavar='json_str_as_argument', dest='', required=False)
    p.add_argument('-f', metavar='input_file', dest='file', required=False)
    return p


def main():
    args = vars(get_option_parser().parse_args(sys.argv[1:]))
    expr = args['expr']
    file_name = args['file']
    if file_name:
        with open(file_name) as f:
            for line in f.readlines():
                line = line.rstrip()
                do_query(line, expr)
    else:
        do_query(sys.stdin.read(), expr)


if __name__ == '__main__':
    main()

