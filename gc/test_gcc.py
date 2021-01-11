import pytest
from gcc import max_gc_seq

def test_max_gc_seq():
    seq = max_gc_seq("gc_sample.txt")
    assert seq[0] == "Rosalind_0808"
    assert seq[1] == pytest.approx(60.919540)
