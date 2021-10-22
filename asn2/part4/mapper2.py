#!/usr/bin/env python3
"""mapper2.py"""

import sys
import os

"""This mapper wants to count the number of words in the documents, so we need to add a 1 to each record"""

for line in sys.stdin:
        line = line.strip()
        # Remember that lines look like term*docName*count
        docName, word, count = line.split("*")
        # Adding the extra 1 to count number of words in the document
        print("%s*%s*%s*%s" % (docName, word, count, 1))