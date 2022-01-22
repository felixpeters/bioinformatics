from .dna import count_nucleotides


def test_count_nucleotides():
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    counts = count_nucleotides(dna)
    assert len(counts) == 4
    assert counts["A"] == 20
    assert counts["C"] == 12
    assert counts["G"] == 17
    assert counts["T"] == 21
