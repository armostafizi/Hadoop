#!/usr/bin/python

import sys

old_key = None
count = 0

for line in sys.stdin:
    this_key, this_count = line.split("\t")

    if old_key and old_key != this_key:
        print "{0}\t{1}".format(old_key, count)
        count = 0

    count += float(this_count)
    old_key = this_key

if old_key:
    print "{0}\t{1}".format(old_key, count)
