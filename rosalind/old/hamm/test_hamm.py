from hamm import calc_hamm_dist

def test_calc_hamm_dist():
    dna1 = "GAGCCTACTAACGGGAT"
    dna2 = "CATCGTAATGACGGCCT"
    assert calc_hamm_dist(dna1, dna2) == 7
