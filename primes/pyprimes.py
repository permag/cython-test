def primes(kmax):
    i = 0
    p = range(5000)
    result = []
    if kmax > 5000:
        kmax = 5000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result