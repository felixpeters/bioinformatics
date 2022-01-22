from pathlib import Path
from .io import parse_fasta


def test_parse_fasta():
    filename = Path(__file__).parent/"data/sample.fasta"
    dna_dict = parse_fasta(filename)
    assert len(dna_dict) == 3
    assert len(dna_dict["Rosalind_6404"]) == 80
    assert len(dna_dict["Rosalind_5959"]) == 84
    assert len(dna_dict["Rosalind_0808"]) == 87
