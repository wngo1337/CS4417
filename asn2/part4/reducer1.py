#!/usr/bin/env python3
"""reducer1.py"""

import sys

current_word = None
current_doc = None
current_count = 0
word = None

# Input comes from STDIN, looks like term*docName*1
for line in sys.stdin:
        line = line.strip()
        fileName, word, count = line.split("*")

        # Convert count to an int
        try:
                count = int(count)
        except ValueError:
                # Count wasn't a number, so discard
                continue

        if current_word == word and current_doc == fileName:
                current_count += count
        else:
                if current_word and current_doc:
                        print("%s*%s*%s" % (current_word, current_doc, current_count))
                current_count = count
                current_word = word
                current_doc = fileName

if current_word == word and current_doc == fileName:
        print("%s*%s*%s" % (current_word, current_doc, current_count))