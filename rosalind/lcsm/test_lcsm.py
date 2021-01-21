from pathlib import Path

from lcsm import shared_motifs, parse_fasta

def test_shared_motifs():
    with open(Path(__file__).absolute().parent / "sample_lcsm.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    seqs = parse_fasta(lines)
    motifs = shared_motifs(seqs)
    assert len(motifs) == 1
