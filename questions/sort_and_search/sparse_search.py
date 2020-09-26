"""
    SPARSE SEARCH (CCI 10.5)

    Given a sorted list of strings that is interspersed with empty strings, write a function to find the location of a
    given string.

    Example:
        Input = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'ball'
        Output = 4

    NOTE:  Ask your interviewer what should happen if someone searches for the empty string.
"""


# Naive Approach:  Time complexity is O(n), where n is the size of l, space complexity is O(1).
def sparse_search_naive(l, s):
    if l is not None and s is not None and len(l) > 0 and len(s) > 0:
        try:
            return l.index(s)
        except:
            return


# NOTE: It DOESN'T matter if l[lo] or l[hi] is '', only a valid l[med] (medium value) is needed!!!


# Optimal Recursive Approach:  Asymptotic time and space is O(log(n)), where n is the length of l.
def sparse_search_rec(l, s):

    def _sparse_search_rec(l, s, lo, hi):
        if lo <= hi:
            med_hi = (lo + hi) // 2
            med_lo = med_hi - 1
            while med_hi <= hi and l[med_hi] == '':
                med_hi += 1
            while lo <= med_lo and l[med_lo] == '':
                med_lo -= 1
            if l[med_hi] == s:
                return med_hi
            elif l[med_lo] == s:
                return med_lo
            elif s < l[med_lo]:
                return _sparse_search_rec(l, s, lo, med_lo - 1)
            else:
                return _sparse_search_rec(l, s, med_hi + 1, hi)

    if l is not None and s is not None and len(l) > 0 and len(s) > 0:
        return _sparse_search_rec(l, s, 0, len(l) - 1)


# Optimal Iterative Approach:  Asymptotic time is O(log(n)), where n is the length of l, asymptotic space is O(1).
def sparse_search(l, s):
    if l is not None and s is not None and len(l) > 0 and len(s) > 0:
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            if lo <= hi:
                med_hi = (lo + hi) // 2
                med_lo = med_hi - 1
                while med_hi <= hi and l[med_hi] == '':
                    med_hi += 1
                while lo <= med_lo and l[med_lo] == '':
                    med_lo -= 1
                if l[med_hi] == s:
                    return med_hi
                elif l[med_lo] == s:
                    return med_lo
                elif s < l[med_lo]:
                    hi = med_lo - 1
                else:
                    lo = med_hi + 1


sorted_list_w_empty_strings = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'hello', '', '', '', '',
                               '', '', '', '', '', '', '', 'world', 'zebra', '']
search_strings = ['hufflepuff', 'ball', 'hello', 'world', '', None]
fns = [sparse_search_naive, sparse_search_rec, sparse_search]

print(f"sorted_list_w_empty_strings: {sorted_list_w_empty_strings}\n")

for s in search_strings:
    print(f"sparse_search_naive(sorted_list_w_empty_strings, {s!r}): {sparse_search_naive(sorted_list_w_empty_strings, s)}")
print()

for s in search_strings:
    print(f"sparse_search_rec(sorted_list_w_empty_strings, {s!r}): {sparse_search_rec(sorted_list_w_empty_strings, s)}")
print()

for s in search_strings:
    print(f"sparse_search(sorted_list_w_empty_strings, {s!r}): {sparse_search(sorted_list_w_empty_strings, s)}")


