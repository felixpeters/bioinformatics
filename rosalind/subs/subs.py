def find_motif(dna, motif):
    locs = []
    for n in range(len(dna) - len(motif) + 1):
        if dna[n:(n+len(motif))] == motif: 
            locs.append(n+1)
    return locs
