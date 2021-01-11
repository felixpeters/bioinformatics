import sys
 
dna = sys.stdin.read().strip()
for i in 'ACGT':
    print(dna.count(i))
