from pathlib import Path

from splc import dna2prot

def test_dna2prot():
    with open(Path(__file__).absolute().parent / "sample_splc.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    prot = dna2prot(lines)
    assert prot == "MVYIADKQHVASREAYGHMFKVCA"
