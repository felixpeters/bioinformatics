def revc(dna):
    tb = dna.maketrans("ACGT", "TGCA")
    return dna[::-1].translate(tb)
