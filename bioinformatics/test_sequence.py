from .sequence import count_nucleotides, gc_content, hamming_distance, reverse_complement, transcribe, translate, find_motif
import numpy as np


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


def test_gc_content():
    dna = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
    gcc = gc_content(dna)
    np.testing.assert_almost_equal(gcc, 0.60919540)


def test_hamming_distance():
    dna1 = "GAGCCTACTAACGGGAT"
    dna2 = "CATCGTAATGACGGCCT"
    assert hamming_distance(dna1, dna2) == 7


def test_translate():
    dna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    rna = translate(dna)
    assert rna == "MAMAPRTEINSTRING"


def test_find_motif():
    dna = "GATATATGCATATACTT"
    motif = "ATAT"
    locs = find_motif(dna, motif)
    assert locs == [1, 3, 9]
