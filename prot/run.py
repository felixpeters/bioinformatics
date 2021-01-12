import sys

from prot import translate_rna

if __name__ == "__main__":
    rna = sys.stdin.read().strip()
    print(translate_rna(rna))
