from typing import Dict, Sequence, Tuple
from collections import Counter
import numpy as np
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


def find_common_ancestor(seqs: Dict[str, str]) -> Tuple[str, np.ndarray]:
    """Finds the most likely common ancestor of the given sequences.

    Args:
        seqs (Dict[str, str]): Dictionary with identifiers as keys and sequences as values (e.g., loaded from FASTA file). Equal length is assumed.

    Returns:
        Tuple[str, np.ndarray]: Consensus string and profile matrix with dimensionality 4x(sequence length)
    """
    seqs = [val for key, val in seqs.items()]
    seq_len = len(seqs[0]) if len(seqs) > 0 else 0
    profile_dict = {n: [0]*len(seqs[0]) for n in "ACGT"}
    seqs_per_pos = ["".join([seq[pos] for seq in seqs])
                    for pos in range(seq_len)]
    for pos in range(seq_len):
        nucleotides = seqs_per_pos[pos]
        for nucleotide in "ACGT":
            profile_dict[nucleotide][pos] = nucleotides.count(nucleotide)
    consensus_string = "".join([Counter(seq).most_common(1)[0][0]
                                for seq in seqs_per_pos])
    profile_matrix = np.array([profile_dict[nucleotide]
                              for nucleotide in "ACGT"])
    return consensus_string, profile_matrix
