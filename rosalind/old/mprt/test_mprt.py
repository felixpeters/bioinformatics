from pathlib import Path

from mprt import motif_locations

def test_motif_locations():
    with open(Path(__file__).absolute().parent / "sample_mprt.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    locs = motif_locations(lines)
    assert len(locs) == 3
    assert len(locs["B5ZC00"]) == 5
