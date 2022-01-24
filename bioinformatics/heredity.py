def dominant_allele_probability(k: int, m: int, n: int) -> float:
    """Calculates probability of receiving at least one dominant allele in offspring from two randomly drawn individuals. Refers to Mendel's first law.

    Args:
        k (int): Number of homozygous dominant individuals
        m (int): Number of heterozygous individuals
        n (int): Number of homozygous recessive individuals

    Returns:
        float: Probability that two randomly selected individuals will produce an individual possessing a dominant allele.
    """
    prob = 0.0
    total = k + m + n
    # cases 1-3: at least one dominant homozygous
    prob += (k / total) + ((m+n)/total) * (k/(total-1))
    # case 4: two heterozygous
    prob += (m/total) * ((m-1)/(total-1)) * (3/4)
    # case 5: one heterozygous, one homozygous recessive
    prob += (m/total) * (n/(total-1))
    return prob
