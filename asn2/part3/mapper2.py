#!/usr/bin/env python3
"""mapper2.py"""

import sys
import os

"""I will be counting the unique bigrams across a corpus, so I will just be displaying a single number"""

# Based on my understanding, we are calculating the number of bigrams that only occur once
# NOT one instance of every bigram?

# Idea is to take the bigram/count pair from first reducer and just map the counts this time
# Then the reducer will sum the counts of 1
for line in sys.stdin:
        line = line.strip()
        # Need to grab count values from text output of reducer1.py
        word1, word2, count = line.split("*")
        print(count)