#!/usr/bin/env python3

import sys
from collections import Counter

data = sys.argv[1]
cnting = {}

for line in open(data):
	if line[0] == '>':
		continue
	else:
		if cnting == {}:
			cnting = Counter(line.rstrip().upper())
		elif cnting != {}:
			cnting += Counter(line.rstrip().upper())

print(cnting)
print(cnting.keys())
print(cnting.values())

print(cnting["A"], cnting["C"], cnting["G"], cnting["T"])
