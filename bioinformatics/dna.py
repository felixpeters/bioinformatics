from typing import Dict


def count_nucleotides(dna: str) -> Dict[str, int]:
    return {n: dna.count(n) for n in "ACGT"}


def transcribe(dna: str) -> str:
    return dna.replace("T", "U")


def reverse_complement(dna: str) -> str:
    translation_table = dna.maketrans("ACGT", "TGCA")
    return dna[::-1].translate(translation_table)


def gc_content(dna: str) -> float:
    return (dna.count("C") + dna.count("G")) / len(dna)
