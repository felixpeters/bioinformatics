from subs import find_motif

def test_find_motif():
    dna = "GATATATGCATATACTT"
    motif = "ATAT"
    assert find_motif(dna, motif) == [2, 4, 10]
