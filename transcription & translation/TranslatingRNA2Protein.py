#!/usr/bin/env python3

def apply_table(string):
	if string == 'A':
		temp = 0
	elif string == 'U':
		temp = 1
	elif string == 'G':
		temp = 2
	elif string == 'C':
		temp = 3

	return temp



data = input("please write the mRNA sequence: ")

#Table, order in 'AUGC' 3 times

F = [[['K', 'N', 'K', 'N'], ['I', 'I', 'M', 'I'], ['R', 'S', 'R', 'S'], ['T', 'T', 'T', 'T']],
     [['/', 'Y', '/', 'Y'], ['L', 'F', 'L', 'F'], ['/', 'C', 'W', 'C'], ['S', 'S', 'S', 'S']],
	 [['E', 'D', 'E', 'D'], ['V', 'V', 'V', 'V'], ['G', 'G', 'G', 'G'], ['A', 'A', 'A', 'A']],
	 [['Q', 'H', 'Q', 'H'], ['L', 'L', 'L', 'L'], ['R', 'R', 'R', 'R'], ['P', 'P', 'P', 'P']]]
	 
print("<Table of mRNA codon to Protein>")

for i in range(0,4):
	for j in range(0,4):
		for k in range(0,4):
			print(F[i][j][k], end=' ')
		print()

print("\n")
idx = 0

while idx<len(data):
	if data[idx] == 'A':
		idx += 1
		if data[idx] == 'U':
			idx += 1
			if data[idx] == 'G':
				break
	idx += 1
	
for times in range(0, len(data)):
	l = times*3+idx-2
	m = times*3+idx-1
	n = times*3+idx
	if n >= len(data) or m >= len(data) or l >= len(data):
		break
	
	i = apply_table(data[l])
	j = apply_table(data[m])
	k = apply_table(data[n])
	
	if F[i][j][k] == '/':
		print()
		break
	else:
		print(F[i][j][k], end='')

print()


'''
for i in range(0,len(data)):
	if data[i] == 'T':
		data[i] = 'U'
	print(data[i], end='')
'''
