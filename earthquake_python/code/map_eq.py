#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',', 12)

    # Ignore invalid lines
    if len(values) != 12:
        continue

    output_key = values[11].replace('"','')
    output_value = float(values[8])

    print("%s\t%s"%(output_key,output_value))

