"""Functionality related to reading and writing files."""

from pathlib import Path
from typing import Dict


def parse_fasta(filename: Path) -> Dict[str, str]:
    """Reads sequences from file in FASTA format.

    Args:
        filename (Path): Path to file

    Returns:
        Dict[str, str]: Dictionary of sequences (uses identifier from file)
    """
    with open(filename) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    dna_dict = {}
    current_key = ""
    for line in lines:
        if line.startswith(">"):
            current_key = line[1:]
            dna_dict[current_key] = ""
        else:
            dna_dict[current_key] += line
    return dna_dict
