#!/usr/bin/env python3
"""mapper1.py"""

import sys
import os
import glob

file_list = list()
path = "/home/cloudera/Documents/asn2/part4/inputDirectory"
# numDocuments = 0

# numDocuments = 0

# Thought I needed this here but I did not
# parameterFile = open("/home/cloudera/Documents/asn2/part4/parameterLocation/inputParameters.txt", "r")
# numDocuments = parameterFile.readline()
# numDocuments = int(numDocuments)

# Grab all text files in the directory
directory_name = glob.gl(b(pa)h+"/*.txt")
for file in directory_name:
        file_list.append(file)

        fileName = os.path.basename(filePointer.name)
        # Reading from file now, not stdin
        for line in filePointer:
                line = line.strip()
                words = line.split()

                for word in words:
                        # What we need from this mapper is each word, the doc it is in, an a count of 1
                        # Like in part 1
                        print("%s*%s*%s" % (word, fileName, 1))