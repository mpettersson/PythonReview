"""
    MOST FREQUENTLY (OCCURRING) ITEM IN LIST

    Write a method to find the most frequently occurring item/element in a list.

    Example:
         Input = [1, 3, 1, 3, 2, 1]
         Output = 1
"""


def most_freq_item(l):
    d = dict()
    mfi = None
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            if mfi is None:
                mfi = i
        if d[mfi] < d[i]:
            mfi = i
    return mfi


l1 = [1, 3, 1, 3, 2, 1]
l2 = [1, 3, 1, 3, 2, 1, 3, 3, 2, 1, 3, 3, 3]
print("l1:", l1)
print("l2:", l2)
print()

print("most_freq_item(l1):", most_freq_item(l1))
print("most_freq_item(l2):", most_freq_item(l2))





