#!/usr/bin/env python3
"""mapper.py"""

import sys
import os
import glob

# Usage: python3 mapper.py | sort | python3 reducer.py

file_list= list()
path = "/home/cloudera/Documents/asn2/part1/inputDirectory"
#The glob function  returns a list of files in a directory matching a pattern

#Here, I decided to open and read the files as noted in the FAQs
directory_name = glob.glob(path+"/*.txt")   # Scan the directory for text files
for file in directory_name:
    file_list.append(file)

#for each file, the lines are printed out
for file in file_list:
    filePointer = open(file)
    fileName = os.path.basename(filePointer.name)   # Getting name of file: store this for output pairs
    # Since we read files, input no longer from stdin
    for line in filePointer:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = line.split()
        # increase counters
        for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # Decided to use "*" as delimiter instead because it seems easier
            print("%s*%s*%s" % (word, fileName, 1))