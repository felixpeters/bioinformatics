import operator

from Bio import SeqIO, SeqUtils

def dna_dict(file):
    fasta_seqs = SeqIO.parse(open(file),'fasta')
    dna_dict = {}
    for seq in fasta_seqs:
        dna_dict[seq.id] = str(seq.seq)
    return dna_dict

def gc_dict(dna_dict):
    gc_dict = {sid: SeqUtils.GC(seq) for sid, seq in dna_dict.items()}
    return gc_dict

def max_gc(gc_dict):
    return max(gc_dict.items(), key=operator.itemgetter(1))

def max_gc_seq(file):
    dd = dna_dict(file)
    gd = gc_dict(dd)
    return max_gc(gd)

