#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Caigao JIANG
# @File    : ProcessItem.py

import json
import redis


def main():
    r = redis.Redis(host='127.0.0.1', port=6378)
    while True:
        source, data = r.blpop(["Base:items"])
        item = json.loads(data)
        try:
            print u"Processig : %(name)s< %(link)s >" % item
        except KeyError:
            print u"Error proccessing:%r" % item

if __name__ == '__main__':
    main()
