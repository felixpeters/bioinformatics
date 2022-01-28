from typing import Dict, Sequence
from .constants import rna_codon_table


def count_nucleotides(dna: str) -> Dict[str, int]:
    return {n: dna.count(n) for n in "ACGT"}


def transcribe(dna: str) -> str:
    return dna.replace("T", "U")


def reverse_complement(dna: str) -> str:
    translation_table = dna.maketrans("ACGT", "TGCA")
    return dna[::-1].translate(translation_table)


def gc_content(seq: str) -> float:
    return (seq.count("C") + seq.count("G")) / len(seq)


def hamming_distance(seq1: str, seq2: str) -> int:
    return sum([i != j for i, j in zip(seq1, seq2)])


def translate(rna: str) -> str:
    """Translate RNA sequence into protein string.

    Args:
        rna (str): RNA sequence

    Returns:
        str: protein string
    """
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    proteins = [rna_codon_table[c] for c in codons]
    protein_string = ''.join(proteins)
    return protein_string.split("Stop", 1)[0]


def find_motif(dna: str, motif: str) -> Sequence[int]:
    """Find all occurrences of a given motif in a DNA string.

    Args:
        dna (str): DNA string
        motif (str): Motif string

    Returns:
        Sequence[int]: Array of starting points
    """
    locs = []
    for n in range(len(dna) - len(motif) + 1):
        if dna[n:(n+len(motif))] == motif:
            locs.append(n)
    return locs
