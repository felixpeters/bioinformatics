import sys
import re
from orf_utils import dna_codon_table as dct

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

def orfs(dna):
    return [m.start() for m in re.finditer("ATG", dna)]

def revc(dna):
    tb = dna.maketrans("ACGT", "TGCA")
    return dna[::-1].translate(tb)

def dna2prot(dna):
    codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
    prots = [dct[c] for c in filter(lambda c: len(c) == 3, codons)]
    prot_str = ''.join(prots)
    if prot_str.find("Stop") != -1:
        return prot_str[:prot_str.find("Stop")]
    else:
        return None

def dna2protcands(lines):
    seqs = parse_fasta(lines)
    seq = seqs[0]["seq"]
    rev = revc(seq)
    starts = orfs(seq)
    pcs = list(filter(lambda p: p != None, [dna2prot(seq[s:]) for s in starts]))
    starts_rev = orfs(rev)
    pcs_rev = list(filter(lambda p: p != None, [dna2prot(rev[s:]) for s in starts_rev]))
    res = list(set(pcs + pcs_rev))
    return res

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    print(*dna2protcands(lines))
