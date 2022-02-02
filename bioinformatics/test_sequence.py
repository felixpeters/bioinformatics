from .sequence import count_nucleotides, find_common_ancestor, gc_content, hamming_distance, longest_common_substrings, reverse_complement, transcribe, translate, find_motif
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


def test_find_common_ancestor():
    seqs = {
        "Rosalind_1": "ATCCAGCT",
        "Rosalind_2": "GGGCAACT",
        "Rosalind_3": "ATGGATCT",
        "Rosalind_4": "AAGCAACC",
        "Rosalind_5": "TTGGAACT",
        "Rosalind_6": "ATGCCATT",
        "Rosalind_7": "ATGGCACT",
    }
    result = np.array([
        [5, 1, 0, 0, 5, 5, 0, 0],
        [0, 0, 1, 4, 2, 0, 6, 1],
        [1, 1, 6, 3, 0, 1, 0, 0],
        [1, 5, 0, 0, 0, 1, 1, 6],
    ])
    consensus_string, profile_matrix = find_common_ancestor(seqs)
    np.testing.assert_array_equal(profile_matrix, result)
    assert consensus_string == "ATGCAACT"
    assert profile_matrix.shape == (4, 8)


def test_longest_common_substrings():
    seqs = {
        "Rosalind_1": "GATTACA",
        "Rosalind_2": "TAGACCA",
        "Rosalind_3": "ATACA",
    }
    result = longest_common_substrings(seqs)
    assert len(result) == 3
    assert "AC" in result
