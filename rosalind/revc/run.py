import sys

from revc import revc

if __name__ == "__main__":
    dna = sys.stdin.read().strip()
    print(revc(dna))
