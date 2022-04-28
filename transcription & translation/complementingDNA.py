#!/usr/bin/env python3

data = input("please write the DNA sequence: ")

print(len(data))
print()

print("\n\n\n")
data = list(data)


for i in range(0, len(data)):
	if data[len(data)-1-i] == 'A':
		print('T', end='')
	elif data[len(data)-1-i] == 'T':
		print('A', end='')
	elif data[len(data)-1-i] == 'G':
		print('C', end='')
	elif data[len(data)-1-i] == 'C':
		print('G', end='')

print('\n\n\n')

print(len(data))
print()

