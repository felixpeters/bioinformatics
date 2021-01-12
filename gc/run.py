import sys

from gcc_scratch import max_gc_seq

if __name__ == "__main__":
    filename = sys.argv[1]
    seq = max_gc_seq(filename)
    print(*seq)

