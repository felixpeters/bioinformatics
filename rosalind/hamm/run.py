import sys

from hamm import calc_hamm_dist

if __name__ == "__main__":
    inputs = sys.stdin.readlines()
    dna1, dna2 = inputs[0].strip(), inputs[1].strip()
    print(calc_hamm_dist(dna1, dna2))
