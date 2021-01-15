def calc_hamm_dist(dna1, dna2):
    dist = 0
    for i, j in zip(dna1, dna2):
        if i != j: dist += 1
    return dist
