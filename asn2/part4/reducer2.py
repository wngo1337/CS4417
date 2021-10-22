#!usr/bin/env python3
"""reducer2.py"""

import sys

current_doc_num_words = 0
current_doc_name = None

currentLineDictionary = {}      # Need to store the lines to append the number of words in the document

for line in sys.stdin:
        line = line.strip()
        word, fileName, count, wordCount = line.split("*")
        currentLine = word + "*" + fileName + "*" + count
        wordNameCount = (word, fileName, count)
        currentLineDictionary[wordNameCount] = currentLine

        try:
                count = int(count)
        except ValueError:
                continue

        if current_doc_name == fileName:
                # Wanted to print out the tuple with the document word count appended, but...
                current_doc_num_words += wordCount
        else:
                if current_doc_name:
                        print(currentLineDictionary[wordNameCount] + "*" + str(current_doc_num_words))
                current_doc_name = fileName