#!/usr/bin/env python

import sys

# Initialize an empty dictionary to store groups and their maximum values
group_max = {}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    value = float(value)


    # Check if the key is already in the dictionary
    if key in group_max:
        group_max[key] = max(group_max[key], value)
    else:
        group_max[key] = value

# Output the maximum values for each group
for key, max_value in group_max.items():
    print("%s\t%s"%(key,max_value))
