import sys
from utils import rna_codon_table as rct

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

def splice(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna

def transcribe(dna):
    return dna.replace("T", "U")

def translate(rna):
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    prots = [rct[c] for c in codons]
    prot_str = ''.join(prots)
    return prot_str.split("Stop", 1)[0]

def dna2prot(lines):
    seqs = parse_fasta(lines)
    dna, introns = seqs[0], seqs[1:]
    dna = splice(dna["seq"], [i["seq"] for i in introns])
    rna = transcribe(dna)
    prot = translate(rna)
    return prot

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.readlines()]
    print(dna2prot(lines))
