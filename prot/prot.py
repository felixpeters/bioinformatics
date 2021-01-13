def rna_codon_table(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    rct = {}
    for line in lines:
        codon, protein = line.split(" ")
        rct[codon] = protein
    return rct

def translate_rna(rna):
    rct = rna_codon_table("rna_codon_table.txt")
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    prots = [rct[c] for c in codons]
    prot_str = ''.join(prots)
    return prot_str.split("Stop", 1)[0]
