#!/usr/bin/python

import sys

stopwords = ['the', 'is', 'and', 'in', 'of', 'a', 'to','in','its','i']

# get all the lines from stdin

for line in sys.stdin:

	# removing all leading and trailing whitespaces

	line = line.strip()

	# split the line into words
	words = line.split()

	filered_words = [text for text in words if text not in stopwords]

	#output tuples in tab-delimited format
	for word in filered_words:
		print("%s\t%s" % (word, "1"))


# Read stopwords from the external file

# stopwords_file = "sw.txt"
# with open(stopwords_file, "r") as f:
#     stopwords = set([line.strip() for line in f])
