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
    return rct
