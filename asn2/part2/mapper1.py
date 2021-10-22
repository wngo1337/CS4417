#!/usr/bin/env python3
"""mapper1.py"""

import sys
import os

"""I am assuming that only one document is going to be piped in, but it shouldn't matter for stdin"""

fullText = ""   # Want to read in every line in input first before gettting bigrams

for line in sys.stdin:
        line = line.strip()
        fullText = fullText + line + " "

# Unfortunately, that adds an extra space after the last line, so I need this ugly thing
fullText = fullText[:-1]

words = fullText.split(" ")     # Now we have all words in a list, so just group by pairs
# Make sure not to go out of index with last word
for i in range(len(words) - 1):
        print("%s*%s*%s" % (words[i], words[i + 1], 1))