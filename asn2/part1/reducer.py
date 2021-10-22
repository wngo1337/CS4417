#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_doc = None
current_count = 0
word = None

# Commented out lines are previous attempts that I wanted to keep just in case
# wordDictionary = {} # To track words and their associated document and count

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
        line = line.strip()

    # parse the input we got from mapper.py
        word, fileName, count = line.split('*')

    # NOW JUST NEED TO FIGURE OUT HOW TO REDUCE (A.K.A. SUM THE TERMS PER DOCUMENT)


# convert count (currently a string) to int
        try:
                count = int(count)
        except ValueError:
    # count was not a number, so silently
    # ignore/discard this line
                continue

        #if (word, fileName) not in wordDictionary:  # Add a pair with count as the value
#        wordDictionary[(word, fileName)] = count
#    else:   # Otherwise an entry exists, so just increment it
#        incrementedCount = int(wordDictionary[(word, fileName)]) + 1
#        wordDictionary[(word, fileName)] = incrementedCount

# for key in wordDictionary:
#    print(key, wordDictionary[key])

# this IF-switch only works because Hadoop sorts map output
#     by key (here: word) before it is passed to the reducer
        if current_word == word and current_doc == fileName:
                current_count += count
        else:
                if current_word and current_doc:
                        # write result to STDOUT
                        print(((current_word, current_doc), current_count))
                current_count = count
                current_word = word
                current_doc = fileName
# do not forget to output the last word if needed!
if current_word == word and current_doc == fileName:
        print(((current_word, current_doc), current_count))