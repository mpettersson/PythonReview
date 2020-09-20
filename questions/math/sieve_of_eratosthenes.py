"""
    SIEVE OF ERATOSTHENES

    SEE: https://rosettacode.org/wiki/Sieve_of_Eratosthenes#Python
"""
import time

# NOTE: The algorithms are ordered in decreasing speed (i.e., slowest at top of file, fastest at bottom of file).


# Basic Sieve of Eratosthenes Approach:
def sieve_of_eratosthenes(n):
    if n:
        n = abs(n)
        if n is 1:
            return []
        l = [True for _ in range(n + 1)]
        l[0] = False
        l[1] = False
        for i in range(2, n+1):
            if l[i]:
                for j in range(2 * i, n + 1, i):
                    l[j] = False
        return [i for i, b in enumerate(l) if b]


# Set Lookup Generator/Iterator Approach:
def iter_primes_via_set(n):
    if n:
        multiples = set()
        for i in range(2, n + 1):
            if i not in multiples:
                yield i
                multiples.update(range(i * i, n + 1, i))


# List Lookup Approach:
def primes_via_list(n):
    if n:
        l = [False] * 2 + [True] * (n - 1)
        for i in range(int(n ** 0.5 + 1.5)):                # Only loop over sqrt of n.
            if l[i]:
                for j in range(i * i, n + 1, i):
                    l[j] = False
        return [i for i, prime in enumerate(l) if prime]


# Odds-Only List Lookup Iterator Approach:
def iter_primes_via_list_odds_only(n):
    if n and n > 1:
        yield 2
        lmtbf = (n - 3) // 2
        l = [True] * (lmtbf + 1)
        for i in range((int(n ** 0.5) - 3) // 2 + 1):
            if l[i]:
                p = i + i + 3
                s = p * (i + 1) + i
                l[s::p] = [False] * ((lmtbf - s) // p + 1)
        for i in range(lmtbf + 1):
            if l[i]:
                yield i + i + 3


# Odds-Only List Lookup Approach:
def primes_via_list_odds_only(n):
    if n:
        if n < 2:
            return []
        if n < 3:
            return [2]
        lmtbf = (n - 3) // 2
        l = [True] * (lmtbf + 1)
        for i in range((int(n ** 0.5) - 3) // 2 + 1):
            if l[i]:
                p = i + i + 3
                s = p * (i + 1) + i
                l[s::p] = [False] * ((lmtbf - s) // p + 1)
        return [2] + [i + i + 3 for i, v in enumerate(l) if v]


# Factorization Wheel235 Generator/Iterator Approach:
def iter_primes_via_wheel_235(n):
    if n and n > 1:
        yield 2
        if n < 3:
            return
        yield 3
        if n < 5:
            return
        yield 5
        if n < 7:
            return
        mod_prms = [7, 11, 13, 17, 19, 23, 29, 31]
        gaps = [4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 4, 6, 2, 6] # 2 loops for overflow
        ndxs = [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7]
        lmtbf = (n + 23) // 30 * 8 - 1                          # integral number of wheels rounded up
        lmtsqrt = (int(n ** 0.5) - 7)
        lmtsqrt = lmtsqrt // 30 * 8 + ndxs[lmtsqrt % 30]        # round down on the wheel
        l = [True] * (lmtbf + 1)
        for i in range(lmtsqrt + 1):
            if l[i]:
                ci = i & 7
                p = 30 * (i >> 3) + mod_prms[ci]
                s = p * p - 7
                p8 = p << 3
                for j in range(8):
                    c = s // 30 * 8 + ndxs[s % 30]
                    l[c::p8] = [False] * ((lmtbf - c) // p8 + 1)
                    s += p * gaps[ci]
                    ci += 1
        for i in range(lmtbf - 6 + (ndxs[(n - 7) % 30])):       # adjust for extras
            if l[i]:
                yield 30 * (i >> 3) + mod_prms[i & 7]


args = [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 100, 101, 1000]
fns = [sieve_of_eratosthenes, iter_primes_via_set, primes_via_list, iter_primes_via_list_odds_only,
       primes_via_list_odds_only, iter_primes_via_wheel_235]

for fn in fns:
    for a in args:
        print(f"{fn.__name__}({a}): {list(fn(a))}")
    print()

n = 10000000
for fn in fns:
    t = time.time(); print(f"{fn.__name__}({n})", end=""); list(fn(n)); print(f" took {time.time() - t} seconds.")


