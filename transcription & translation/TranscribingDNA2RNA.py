#!/usr/bin/env python3

data = input("please write the DNA sequence: ")

data = list(data)

for i in range(0,len(data)):
	if data[i] == 'T':
		data[i] = 'U'
	print(data[i], end='')

