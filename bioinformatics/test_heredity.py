import numpy as np
from .heredity import dominant_allele_probability, mortal_fibonacci


def test_dominant_allel_probability():
    k, m, n = 2, 2, 2
    prob = dominant_allele_probability(k, m, n)
    np.testing.assert_almost_equal(prob, 0.78333, decimal=5)


def test_mortal_fibonacci():
    actual = mortal_fibonacci(6, 3)
    desired = 4
    assert actual == desired
