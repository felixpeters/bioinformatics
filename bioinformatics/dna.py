from typing import Dict

def count_nucleotides(dna: str) -> Dict[str, int]:
    return {n: dna.count(n) for n in "ACGT"}