from pathlib import Path

from orf import dna2protcands

def test_dna2prot():
    with open(Path(__file__).absolute().parent / "sample_orf.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    pcs = dna2protcands(lines)
    assert len(pcs) == 4
    assert sorted([len(s) for s in pcs]) == [1, 12, 14, 26]
