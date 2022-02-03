"""Functionality related to working with sequences, e.g., DNA and RNA strings."""

from typing import Dict, Sequence, Tuple
import re
from collections import Counter
import numpy as np
from .constants import rna_codon_table


def count_nucleotides(dna: str) -> Dict[str, int]:
    """Count nucleotides in given DNA string.

    Args:
        dna (str): DNA string

    Returns:
        Dict[str, int]: Count per nucleotide
    """
    return {n: dna.count(n) for n in "ACGT"}


def transcribe(dna: str) -> str:
    """Transcribe DNA into RNA string.

    Args:
        dna (str): DNA string

    Returns:
        str: RNA string
    """
    return dna.replace("T", "U")


def reverse_complement(dna: str) -> str:
    """Generate reverse complement of given DNA string.

    Args:
        dna (str): DNA string

    Returns:
        str: Reverse complement string
    """
    translation_table = dna.maketrans("ACGT", "TGCA")
    return dna[::-1].translate(translation_table)


def gc_content(seq: str) -> float:
    """Calculate relative GC content of given sequence.

    Args:
        seq (str): Sequence string

    Returns:
        float: Percentage of G and C nucleotides
    """
    return (seq.count("C") + seq.count("G")) / len(seq)


def hamming_distance(seq1: str, seq2: str) -> int:
    """Calculate Hamming distance of given sequences.

    Args:
        seq1 (str): First sequence
        seq2 (str): Second sequence

    Returns:
        int: Number of differing nucleotides
    """
    return sum([i != j for i, j in zip(seq1, seq2)])


def translate(rna: str) -> str:
    """Translate RNA sequence into protein string.

    Args:
        rna (str): RNA sequence

    Returns:
        str: protein string (empty string if no stop codon is present)
    """
    codons = [rna[i:i+3] for i in range(0, len(rna)//3 * 3, 3)]
    proteins = [rna_codon_table[c] for c in codons]
    protein_string = ''.join(proteins)
    if "Stop" not in protein_string:
        return ""
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
    for pos in range(len(dna) - len(motif) + 1):
        if dna[pos:(pos+len(motif))] == motif:
            locs.append(pos)
    return locs


def find_common_ancestor(seqs: Dict[str, str]) -> Tuple[str, np.ndarray]:
    """Finds the most likely common ancestor of the given sequences.

    Args:
        seqs (Dict[str, str]): Dictionary with (identifier, sequence), e.g., from FASTA file.
                                Equal length is assumed.

    Returns:
        Tuple[str, np.ndarray]: Consensus string and profile matrix (dim 4x(sequence length))
    """
    seqs = [val for _, val in seqs.items()]
    seq_len = len(seqs[0]) if len(seqs) > 0 else 0
    profile_matrix_dict = {nuc: [0]*len(seqs[0]) for nuc in "ACGT"}
    # take transpose of sequences to enable counting
    nucs_per_pos = ["".join([seq[pos] for seq in seqs])
                    for pos in range(seq_len)]
    for pos in range(seq_len):
        for nuc in "ACGT":
            profile_matrix_dict[nuc][pos] = nucs_per_pos[pos].count(
                nuc)
    consensus_string = "".join([Counter(seq).most_common(1)[0][0]
                                for seq in nucs_per_pos])
    profile_matrix_arr = np.array([profile_matrix_dict[nuc]
                                   for nuc in "ACGT"])
    return consensus_string, profile_matrix_arr


def longest_common_substrings(seqs: Dict[str, str]) -> Sequence[str]:
    """Finds the longest common substrings in a collection of sequences.

    Args:
        seqs (Dict[str, str]): Dictionary with sequences in (identifier, sequence) format.

    Returns:
        Sequence[str]: Longest common substrings with same length
    """
    results = []
    # find shortest string as base sequences
    seqs = [val for _, val in seqs.items()]
    seqs.sort(key=len)
    base_seq, comp_seqs = seqs[0], seqs[1:]
    # iterate through string lengths, starting with length of shortest string
    for seq_len in range(len(base_seq), 0, -1):
        # initialize cache for previous searches
        previous_searches = []
        # iterate through all possible substrings of current length
        for pos in range(0, len(base_seq) - seq_len + 1):
            substr = base_seq[pos:(pos+seq_len)]
            if substr not in previous_searches:
                # add substring to results if contained in all sequences
                if all((substr in seq for seq in comp_seqs)):
                    results.append(substr)
                # cache current search in order to avoid duplicates
                previous_searches.append(substr)
        if len(results) > 0:
            break
    return results


def find_open_reading_frames(dna: str) -> Sequence[str]:
    """Finds all possible reading frames for a given sequence.
        Checks only for start codon, not for stop codon.

    Args:
        dna (str): DNA string

    Returns:
        Sequence[str]: Array of possible reading frames
    """
    return [dna[m.start():] for m in re.finditer("ATG", dna)]


def find_candidate_proteins(dna: str) -> Sequence[str]:
    """Finds every distinct candidate protein string from the given sequence.
        Searches all open reading frames of the given sequence and its reverse complement.


    Args:
        dna (str): DNA string

    Returns:
        Sequence[str]: Array of protein candidates
    """
    proteins = set()
    strands = [dna, reverse_complement(dna)]
    for strand in strands:
        orfs = find_open_reading_frames(strand)
        for orf in orfs:
            protein = translate(transcribe(orf))
            if len(protein) > 0:
                proteins.add(protein)
    return list(proteins)
