import sys

sequence = sys.argv[1]
seq = ''
count_A =0
count_C = 0
count_G = 0
count_T = 0

for line in open(sequence):
    if line[0] == '>':
        continue

    else:   # line[0] != '>'
        seq += line.rstrip().upper()

for i in range(0, len(seq)):
    nt = seq[i]
    
    if nt == 'A':
        count_A += 1

    elif nt == 'C':
        count_C += 1
    
    elif nt == 'G':
        count_G += 1
    
    else:   #nt =='T'
        count_T += 1

print(count_A, count_C, count_G, count_T)