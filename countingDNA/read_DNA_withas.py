#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file:
	data = "".join([line.rstrip().upper() for line in file if line[0]!='>'])

print(data)

A = 0
C = 0
G = 0
T = 0

for i in range(0, len(data)):
	if data[i] == 'A':
		A += 1
	elif data[i] == 'C':
		C += 1
	elif data[i] == 'G':
		G += 1
	else: 	#data[i]=='T'
		T += 1

print(A, C, G, T)

