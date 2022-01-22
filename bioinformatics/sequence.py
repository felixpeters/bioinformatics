from typing import Dict


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
