#!/usr/bin/env python3

def apply_ATGC_Table(sequence_length):
	F = [[0 for i in range(sequence_length)] for j in range(4)]
	#F[0]:'A', F[1]:'T', F[2]:'G', F[3]:'C'
	return F

def apply_protein_Table(sequence_length):
	F = [[0 for i in range(sequence_length)] for j in range(20)]
	#row: A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y
	return F

def scoring_ATGC(List, alignment_number):
	A,T,G,C = 0,0,0,0
	for i in range(1, alignment_number):
		if List[i] == 'A': A += 1
		elif List[i] == 'T': T += 1
		elif List[i] == 'G': G += 1
		else: C += 1	#List[i] == 'C'
	return A/i,T/i,G/i,C/i

def scoring_protein(List, alignment_number):
	A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
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
		
	return A/i,C/i,D/i,E/i,F/i,G/i,H/i,I/i,K/i,L/i,M/i,N/i,P/i,Q/i,R/i,S/i,T/i,V/i,W/i,Y/i

#main code
import pandas as pd

data = ''
aln_num = 0
case = 0

#DNA PSSM or Protein PSSM
while case != 1 and case != 2:
	case = int(input("Choose PSSM type (DNA PSSM - 1, Protein PSSM - 2) : "))
	if case != 1 and case != 2:
		print("case is not in the choice, choose a number again")


data = input("Please wirte the Query Sequence(motif) : ")
length = len(data)
L, Temp = [], []

while data!='done':
	L.append(data)
	aln_num += 1

	if data == 'done':
		break
	elif len(data) != length:
		print("length of the sequence is different")
		L.remove(data)
		aln_num -= 1
	
	data = input("Please wirte the Alignment(done==exit) : ")

#Printing Sequence
print("\n<Sequences>")
for i in range(0, aln_num):
	print(i+1,"sequence :", L[i])

#DNA PSSM
if case == 1:
	F = apply_ATGC_Table(length)

	for i in range(0, length):
		for j in range(0, aln_num):
			Temp.append(L[j][i])

		F[0][i],F[1][i],F[2][i],F[3][i] = scoring_ATGC(Temp, aln_num)
		Temp = []

	PSSM = {'A':F[0], 'T':F[1], 'G':F[2], 'C':F[3]}
	origin_col = ['A','T','G','C']

#Protein PSSM
else:	#case == 2
	F = apply_protein_Table(length)
	
	for i in range(0, length):
		for j in range(0, aln_num):
			Temp.append(L[j][i])
	
		F[0][i],F[1][i],F[2][i],F[3][i],F[4][i],F[5][i],F[6][i],F[7][i],F[8][i],F[9][i],F[10][i],F[11][i],F[12][i],F[13][i],F[14][i],F[15][i],F[16][i],F[17][i],F[18][i],F[19][i] = scoring_protein(Temp, aln_num)
		Temp = []

	PSSM = {'A':F[0],'C':F[1],'D':F[2],'E':F[3],'F':F[4],'G':F[5],'H':F[6],'I':F[7],'K':F[8],'L':F[9],'M':F[10],'N':F[11],'P':F[12],'Q':F[13],'R':F[14],'S':F[15],'T':F[16],'V':F[17],'W':F[18],'Y':F[19]}
	origin_col = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']


#Printing PSSM
sj = pd.DataFrame(PSSM, index=[i for i in range(1, length+1)], columns=origin_col)
sj.index.name = 'seq loc'
print("\n<PSSM Table>")
print(sj)
