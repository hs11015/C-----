#!/usr/bin/env python3

#Initializing DNA PSI-BLAST scoring Table function
def apply_ATGC_Table(sequence_length):
	F = [[0 for i in range(sequence_length)] for j in range(4)]
	#F[0]:'A', F[1]:'T', F[2]:'G', F[3]:'C'
	return F


#making DNA position probility * score matrix
def scoring_ATGC(List, alignment_number, query, score):
	#preventing zero nucleotide, +0.25 each of them. TOTAL 1
	A,T,G,C,idx = 0.25,0.25,0.25,0.25,0
	for i in range(0, alignment_number):
		if List[i] == 'A': A += 1
		elif List[i] == 'T': T += 1
		elif List[i] == 'G': G += 1
		else: C += 1	#List[i] == 'C'

	if query == 'A': idx = 0
	elif query == 'T': idx = 1
	elif query == 'G': idx = 2
	elif query == 'C': idx = 3
	
	i += 1

	A = A/i * score[idx][0]
	T = T/i * score[idx][1]
	G = G/i * score[idx][2]
	C = C/i * score[idx][3]

	return A,T,G,C





#main code
import pandas as pd
import sys
import random

database = sys.argv[1]
score_matrix = sys.argv[2]


# loading the sequences

data = []
seq_temp = ''
seq_num = 0

for line in open(database):
	line = line.rstrip()
	if line[0] == ">":
		if len(seq_temp) > 0:
			data.append(seq_temp)

		seq_num += 1
		seq_temp = ''

	else:
		seq_temp += line.rstrip().upper()

#if the line is last line of the file(sequence)
data.append(seq_temp)



# loading the score matrix
score = [[0 for i in range(4)] for j in range(4)]
line_num = 0

for line in open(score_matrix):
	temp = line.rstrip().split() #split by ' '

	for i in range(4):
		score[line_num][i] = float(temp[i])

	line_num += 1



#Printing Sequence
print("\n<Sequences>")
for i in range(0, seq_num):
	print(i+1,"\tsequence :", data[i])
print()



#Choosing a Query Sequence(motif)
query = int(input("Please choose a Query Sequence(motif) : "))
query_seq = data[query-1]

#data.remove(query_seq)
#seq_num -= 1

length = len(data[0])
Temp = []




#DNA PSSM
F = apply_ATGC_Table(length)

for i in range(0, length):
	for j in range(0, seq_num):
		Temp.append(data[j][i])
			
	nucleotide = query_seq[i]
	F[0][i],F[1][i],F[2][i],F[3][i] = scoring_ATGC(Temp, seq_num, nucleotide, score)
	Temp = []

PSSM = {'A':F[0], 'T':F[1], 'G':F[2], 'C':F[3]}
origin_col = ['A','T','G','C']






#Printing PSSM
sj = pd.DataFrame(PSSM, index=[i for i in range(1, length+1)], columns=origin_col)
sj.index.name = 'seq loc'
print("\n<PSSM Table>")
print(sj)



#printing the Best score and Consensus motif
best_score = 0
best_score_sum = 0
temp_nt = ''
consensus_motif = ''
other_seq_num = 1

for i in range(length):
	best_score = max(F[0][i],F[1][i],F[2][i],F[3][i])
	if best_score == F[0][i]:
		temp_nt += 'A'
	if best_score == F[1][i]:
		temp_nt += 'T'
	if best_score == F[2][i]:
		temp_nt += 'G'
	if best_score == F[3][i]:
		temp_nt += 'C'
	
	other_seq_num *= len(temp_nt)
	consensus_motif += random.choice(temp_nt)
	best_score_sum += best_score
	temp_nt = ''


print("\n<RESULT>\n")
print("Best scores :", best_score_sum)
print("Consensus motif :", consensus_motif)
print("There are other", other_seq_num-1, "consensus motifs.\n")
