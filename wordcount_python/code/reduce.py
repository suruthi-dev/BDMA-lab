#!/usr/bin/python

import sys

# grouping the words using dictionary

word2count = {}

for line in sys.stdin:
	line = line.strip()
	
	word, count = line.split("\t",1)
	
	try :
		count = int(count)
	except ValueError:
		continue

	try:
		word2count[word] = word2count[word]+1
	except:
		word2count[word] = 1


for words in word2count.keys():
	print("%s\t%s"%(words,word2count[words]))
