#!/usr/bin/python2.7
from optparse import OptionParser
from collections import defaultdict


def printStuff(fn):
	f = open(fn)
	b = 'I'
	for line in f.readlines():
		b += 'I'
		for num in line.split():
			for i in range(int(num)):
				b += 'a'
			b += 'I'

	b += 'I'
	print b
		
(_, args) = OptionParser().parse_args()

for fn in args:
	printStuff(fn)
