#!/usr/bin/env python3

#Protein PSI-BLAST scoring Table function
def apply_protein_Table(sequence_length):
	F = [[0 for i in range(sequence_length)] for j in range(20)]
	#row: A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y
	return F


#making Protein position probility * score matrix
def scoring_protein(List, alignment_number, query, score):
	A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y = 0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05
	for i in range(1, alignment_number):
		if List[i] == 'A': A += 1
		elif List[i] == 'C': C += 1
		elif List[i] == 'D': D += 1
		elif List[i] == 'E': E += 1
		elif List[i] == 'F': F += 1
		elif List[i] == 'G': G += 1
		elif List[i] == 'H': H += 1
		elif List[i] == 'I': I += 1
		elif List[i] == 'K': K += 1
		elif List[i] == 'L': L += 1
		elif List[i] == 'M': M += 1
		elif List[i] == 'N': N += 1
		elif List[i] == 'P': P += 1
		elif List[i] == 'Q': Q += 1
		elif List[i] == 'R': R += 1
		elif List[i] == 'S': S += 1
		elif List[i] == 'T': T += 1
		elif List[i] == 'V': V += 1
		elif List[i] == 'W': W += 1
		else: Y += 1    #List[i] == 'Y'
	
	
	if query == 'A': idx = 0
	elif query == 'C': idx = 1
	elif query == 'D': idx = 2
	elif query == 'E': idx = 3
	elif query == 'F': idx = 4
	elif query == 'G': idx = 5
	elif query == 'H': idx = 6
	elif query == 'I': idx = 7
	elif query == 'K': idx = 8
	elif query == 'L': idx = 9
	elif query == 'M': idx = 10
	elif query == 'N': idx = 11
	elif query == 'P': idx = 12
	elif query == 'Q': idx = 13
	elif query == 'R': idx = 14
	elif query == 'S': idx = 15
	elif query == 'T': idx = 16
	elif query == 'V': idx = 17
	elif query == 'W': idx = 18
	else: idx = 19    #List[i] == 'Y'


	#To prevent zero score, add 0.05 each. TOTAL 1
	i += 1
	A = A/i# * score[idx][0]
	C = C/i# * score[idx][1]
	D = D/i# * score[idx][2]
	E = E/i# * score[idx][3]
	F = F/i# * score[idx][4]
	G = G/i# * score[idx][5]
	H = H/i# * score[idx][6]
	I = I/i# * score[idx][7]
	K = K/i# * score[idx][8]
	L = L/i# * score[idx][9]
	M = M/i# * score[idx][10]
	N = N/i# * score[idx][11]
	P = P/i# * score[idx][12]
	Q = Q/i# * score[idx][13]
	R = R/i# * score[idx][14]
	S = S/i# * score[idx][15]
	T = T/i# * score[idx][16]
	V = V/i# * score[idx][17]
	W = W/i# * score[idx][18]
	Y = Y/i# * score[idx][19]

	return A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y




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
score = [[0 for i in range(20)] for j in range(20)]
line_num = 0


for line in open(score_matrix):
	temp = line.rstrip().split() #split by ' '

	for i in range(20):
		score[line_num][i] = float(temp[i])

	line_num += 1



#Printing Sequence
print("\n<Sequences>")
for i in range(0, seq_num):
	print(i+1,"sequence :", data[i])
print()



#Choosing a Query Sequence(motif)
query = int(input("Please choose a Query Sequence(motif) : "))
query_seq = data[query-1]

#data.remove(query_seq)
#seq_num -= 1

length = len(data[0])
Temp = []




#DNA PSSM
F = apply_protein_Table(length)

for i in range(0, length):
	for j in range(0, seq_num):
		Temp.append(data[j][i])
			
	protein = query_seq[i]
	F[0][i],F[1][i],F[2][i],F[3][i],F[4][i],F[5][i],F[6][i],F[7][i],F[8][i],F[9][i],F[10][i],F[11][i],F[12][i],F[13][i],F[14][i],F[15][i],F[16][i],F[17][i],F[18][i],F[19][i] = scoring_protein(Temp, seq_num, protein, score)
	Temp = []

	PSSM = {'A':F[0],'C':F[1],'D':F[2],'E':F[3],'F':F[4],'G':F[5],'H':F[6],'I':F[7],'K':F[8],'L':F[9],'M':F[10],'N':F[11],'P':F[12],'Q':F[13],'R':F[14],'S':F[15],'T':F[16],'V':F[17],'W':F[18],'Y':F[19]}			    
	origin_col = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']





#Printing PSSM
sj = pd.DataFrame(PSSM, index=[i for i in range(1, length+1)], columns=origin_col)
sj.index.name = 'seq loc'
print("\n<Probability Table>")
print(sj)



#printing the Best score and Consensus motif
best_score = 0
best_score_sum = 0
temp_nt = ''
consensus_motif = ''
other_seq_num = 1

for i in range(length):
	best_score = max(F[0][i],F[1][i],F[2][i],F[3][i],F[4][i],F[5][i],F[6][i],F[7][i],F[8][i],F[9][i],F[10][i],F[11][i],F[12][i],F[13][i],F[14][i],F[15][i],F[16][i],F[17][i],F[18][i],F[19][i])
	
	if best_score == F[0][i]:
		temp_nt += 'A'
	if best_score == F[1][i]:
		temp_nt += 'C'
	if best_score == F[2][i]:
		temp_nt += 'D'
	if best_score == F[3][i]:
		temp_nt += 'E'
	if best_score == F[4][i]:
		temp_nt += 'F'
	if best_score == F[5][i]:
		temp_nt += 'G'
	if best_score == F[6][i]:
		temp_nt += 'H'
	if best_score == F[7][i]:
		temp_nt += 'I'
	if best_score == F[8][i]:
		temp_nt += 'K'
	if best_score == F[9][i]:
		temp_nt += 'L'
	if best_score == F[10][i]:
		temp_nt += 'M'
	if best_score == F[11][i]:
		temp_nt += 'N'
	if best_score == F[12][i]:
		temp_nt += 'P'
	if best_score == F[13][i]:
		temp_nt += 'Q'
	if best_score == F[14][i]:
		temp_nt += 'R'
	if best_score == F[15][i]:
		temp_nt += 'S'
	if best_score == F[16][i]:
		temp_nt += 'T'
	if best_score == F[17][i]:
		temp_nt += 'V'
	if best_score == F[18][i]:
		temp_nt += 'W'
	if best_score == F[18][i]:
		temp_nt += 'Y'

	other_seq_num *= len(temp_nt)
	consensus_motif += random.choice(temp_nt)
	best_score_sum += best_score
	temp_nt = ''


print("\n<RESULT>\n")
print("Best scores :", best_score_sum)
print("Consensus motif :", consensus_motif)
print("There are other", other_seq_num-1, "consensus motifs.\n")
