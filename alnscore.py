#!/usr/bin/env python3
import sys

fpath = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])
gap = int(sys.argv[4])

dic_seqs = {}
seq = ''
spc = ''

for line in open(fpath):
	if line[0] == '>':
		if len(seq) > 0:
			dic_seqs[spc] = seq

		spc = line.rstrip()[1:]	#exclude the first letter, '>'
		seq=''
	else:	#line is not started with '>'
		seq += line.rstrip().upper()

		#if the line is last line of the file(sequence)
		if line[len(line)-2:len(line)-1] != '\n':
			dic_seqs[spc] = seq

[seq1, seq2] = dic_seqs.values()
print("1st sequence :", seq1)
print("2nd sequence :", seq2)

score = 0

for i in range(0, len(seq1)):
	nt1 = seq1[i]
	nt2 = seq2[i]

	#if nt1 and nt2 both of them '-'?

	if nt1 == '-' or nt2 =='-':
		score += gap

	elif nt1 == nt2:
		score += match
	
	else:	#nt1 != nt2
		score += mismatch

print("alignment score is", score)
