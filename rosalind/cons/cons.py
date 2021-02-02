import sys
from collections import Counter
import numpy as np

def parse_fasta(lines):
    seqs = []
    cur_seq = None
    for line in lines:
        if line.startswith(">"):
            if cur_seq: seqs.append(cur_seq)
            cur_seq = {
                    "id": line[1:],
                    "seq": "",
            }
        else:
            cur_seq["seq"] += line
    seqs.append(cur_seq)
    return seqs

def consensus(seqs):
    seqs = [seq["seq"] for seq in seqs]
    seq_len = len(seqs[0]) if len(seqs) > 0 else 0
    prof = {n: [0]*len(seqs[0]) for n in "ACGT"}
    pos_seqs = ["".join([seq[pos] for seq in seqs]) for pos in range(seq_len)]
    for pos in range(seq_len):
        nucs = pos_seqs[pos]
        for nuc in "ACGT":
            prof[nuc][pos] = nucs.count(nuc)
    # TODO: return most common symbol at each position
    cons = "".join([Counter(seq).most_common(1)[0][0] for seq in pos_seqs])
    return cons, prof 

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    seqs = parse_fasta(lines)
    cons, prof = consensus(seqs)
    print(cons)
    for key, val in prof.items():
        print(f"{key}:", *val)
