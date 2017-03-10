#!/usr/bin/python

import csv
import sys

def replace_chars(s):
    replacing_chars = ".,!?:;\"()<>[]#$=-/"
    for char in replacing_chars:
        s = s.replace(char, " ")
    return s


reader = csv.reader(sys.stdin, delimiter = "\t")
reader.next()

for row in reader:
    body = row[4]
    body = replace_chars(body)
    words = body.split()
    for word in words:
        print "{0}\t{1}".format(word.lower(), 1)
