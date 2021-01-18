def pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return  pairs(n-1, k) + k * pairs(n-2, k)
