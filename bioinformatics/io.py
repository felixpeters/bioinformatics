from pathlib import Path
from typing import Dict


def parse_fasta(filename: Path) -> Dict[str, str]:
    with open(filename) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    dna_dict = {}
    current_key = ""
    for line in lines:
        if line.startswith(">"):
            current_key = line[1:]
            dna_dict[current_key] = ""
        else:
            dna_dict[current_key] += line
    return dna_dict
