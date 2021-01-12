import pytest
from gcc import max_gc_seq
from gcc_scratch import max_gc_seq as max_gc_seq_scratch

def test_max_gc_seq():
    seq = max_gc_seq("gc_sample.txt")
    assert seq[0] == "Rosalind_0808"
    assert seq[1] == pytest.approx(60.919540)

def test_max_gc_seq_scratch():
    seq = max_gc_seq("gc_sample.txt")
    seq_scratch = max_gc_seq_scratch("gc_sample.txt")
    assert seq[0] == seq_scratch[0]
    assert seq[1] == pytest.approx(seq_scratch[1])
