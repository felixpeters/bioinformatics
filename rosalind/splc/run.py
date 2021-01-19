import sys

from splc import dna2prot

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    print(dna2prot(lines))
