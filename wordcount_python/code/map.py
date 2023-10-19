#!/usr/bin/python

import sys

# get all the lines from stdin

for line in sys.stdin:

	# removing all leading and trailing whitespaces

	line = line.strip()

	# split the line into words
	words = line.split()

	#output tuples in tab-delimited format
	for word in words:
		print("%s\t%s" % (word, "1"))
