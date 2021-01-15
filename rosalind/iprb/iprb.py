def calc_prob(k, m, n):
    prob = 0.0
    total = k + m + n
    # cases 1-3: at least one dominant homozygous
    prob += (k / total) + ((m+n)/total) * (k/(total-1))
    # case 4: two heterozygous
    prob += (m/total) * ((m-1)/(total-1)) * (3/4)
    # case 5: one heterozygous, one homozygous recessive
    prob += (m/total) * (n/(total-1))
    return round(prob, 5)
