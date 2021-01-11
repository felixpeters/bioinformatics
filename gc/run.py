import sys

from gcc import max_gc_seq

if __name__ == "__main__":
    file = sys.argv[1]
    seq = max_gc_seq(file)
    print(*seq)

