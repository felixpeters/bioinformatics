"""Functions related to heredity, i.e., the inheritance of traits."""


def dominant_allele_probability(n_homo_dom: int, n_hetero: int, n_homo_rec: int) -> float:
    """Calculates probability of receiving at least one dominant allele in offspring
        from two randomly drawn individuals. Refers to Mendel's first law.

    Args:
        n_homo_dom (int): Number of homozygous dominant individuals
        n_hetero (int): Number of heterozygous individuals
        n_homo_rec (int): Number of homozygous recessive individuals

    Returns:
        float: Calculated probability
    """
    prob = 0.0
    total = n_homo_dom + n_hetero + n_homo_rec
    # cases 1-3: at least one dominant homozygous
    prob += (n_homo_dom / total) + \
        ((n_hetero+n_homo_rec)/total) * (n_homo_dom/(total-1))
    # case 4: two heterozygous
    prob += (n_hetero/total) * ((n_hetero-1)/(total-1)) * (3/4)
    # case 5: one heterozygous, one homozygous recessive
    prob += (n_hetero/total) * (n_homo_rec/(total-1))
    return prob


def mortal_fibonacci(periods: int, lifespan: int) -> int:
    """Calculates the number of pairs after given number of periods. 
        Pairs live for the given lifespan and produce one offspring per period.

    Args:
        periods (int): Experiment duration
        lifespan (int): Lifetime of one pair

    Returns:
        int: Number of pairs after given number of periods
    """
    pairs = [1, 1]
    period = 2
    # decrease periods by one to enable array indexing
    periods -= 1
    while period <= periods:
        if period < lifespan:
            pairs.append(pairs[-2] + pairs[-1])
        elif period == lifespan or period == (lifespan + 1):
            pairs.append(pairs[-2] + pairs[-1] - 1)
        else:
            pairs.append(pairs[-2] + pairs[-1] - pairs[-(lifespan + 1)])
        period += 1
    return pairs[-1]
