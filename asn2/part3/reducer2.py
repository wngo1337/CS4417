#!/usr/bin/env python3
"""reducer2.py"""

import sys

current_count = 0
unique_count = 0

for line in sys.stdin:
        try:
                current_count = int(line)
        except ValueError:
                # This should never happen, but I guess if there is an invalid input, just skip it
                continue

        if (current_count == 1):
                unique_count += current_count
        else:
                if current_count:
                        continue

print(unique_count)