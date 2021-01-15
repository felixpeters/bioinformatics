import pytest
from iprb import calc_prob

def test_calc_prob():
    k, m, n = 2, 2, 2
    assert calc_prob(k, m , n) == pytest.approx(0.78333, abs=1e-6)
