from .dna import count_nucleotides, reverse_complement, transcribe


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


def test_reverse_complement():
    dna = "AAAACCCGGT"
    revc = reverse_complement(dna)
    assert revc == "ACCGGGTTTT"
