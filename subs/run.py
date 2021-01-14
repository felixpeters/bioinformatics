import sys

from subs import find_motif

if __name__ == "__main__":
    inputs = sys.stdin.readlines()
    dna, motif = inputs[0].strip(), inputs[1].strip()
    print(*find_motif(dna, motif))
