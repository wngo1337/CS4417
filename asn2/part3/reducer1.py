#!/usr/bin/env python3
"""reducer1.py"""

import sys

# bigramDictionary = {}

# Slightly modified output of this reducer for ease of use in mapper2.py

current_bigram = None
current_count = 0
bigram = None

for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # Parse the input we got from mapper.py
        word1, word2, count = line.split("*")
        bigram = (word1, word2)

        # Convert count (currently a string) to int
        try:
                count = int(count)
        except ValueError:
                # count was a number, so silently
                # ignore/discard this line
                continue

        if current_bigram == bigram:
                current_count += count
        else:
                if current_bigram:
                        # write result to STDOUT
                        print("%s*%s*%s" % (current_bigram[0], current_bigram[1], current_count))

                current_count = count
                current_bigram = bigram

# do not forget to output the last bigram if needed!
# if current_bigram == bigram:
#       print((bigram, current_count))



#       if bigram not in bigramDictionary:
#               bigramDictionary[bigram] = count
#       else:
#               incrementedCount = bigramDictionary[bigram] + 1
#               bigramDictionary[bigram] = incrementedCount

# for bigram in bigramDictionary:
#       print((bigram[0], bigram[1]), bigramDictionary[bigram])