import sys
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

def concensus(seqs):
    seqs = [seq["seq"] for seq in seqs]
    seq_len = len(seqs[0]) if len(seqs) > 0 else 0
    prof = {n: [0]*len(seqs[0]) for n in "ACGT"}
    for pos in range(seq_len):
        nucs = "".join([seq[pos] for seq in seqs])
        for nuc in "ACGT":
            prof[nuc][pos] = nucs.count(nuc)
    print(prof)
    # TODO: return most common symbol at each position
    cons = ""
    return cons, prof 

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    seqs = parse_fasta(lines)
    print(concensus(seqs))
