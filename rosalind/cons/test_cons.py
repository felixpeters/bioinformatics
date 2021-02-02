from pathlib import Path
from cons import parse_fasta, concensus

def test_concensus():
    with open(Path(__file__).absolute().parent / "sample_cons.fasta") as f:
        lines = [l.strip() for l in f.readlines()]
    seqs = parse_fasta(lines)
    assert len(seqs) == 7
    cons, prof = concensus(seqs)
    assert prof["A"] == [5, 1, 0, 0, 5, 5, 0, 0]
    assert prof["C"] == [0, 0, 1, 4, 2, 0, 6, 1]
    assert prof["G"] == [1, 1, 6, 3, 0, 1, 0, 0]
    assert prof["T"] == [1, 5, 0, 0, 0, 1, 1, 6]
    assert cons == "ATGCAACT"
