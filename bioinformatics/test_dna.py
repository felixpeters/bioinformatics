from .dna import count_nucleotides, transcribe


def test_count_nucleotides():
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    counts = count_nucleotides(dna)
    assert len(counts) == 4
    assert counts["A"] == 20
    assert counts["C"] == 12
    assert counts["G"] == 17
    assert counts["T"] == 21


def test_transcribe():
    dna = "GATGGAACTTGACTACGTAAATT"
    rna = transcribe(dna)
    assert rna == "GAUGGAACUUGACUACGUAAAUU"
