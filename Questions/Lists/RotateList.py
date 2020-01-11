"""
    ROTATE A LIST (ARRAY)

    Given a list l and an int y rotate the values of the list y times to the right (rotate_right) or y times to
    the left (rotate_left).
"""

l = [1, 2, 3, 4, 5]


def rotate_left(l, y=1):
    if len(l) <= 1:
        return l
    y = y % len(l)
    return l[y:] + l[:y]


def rotate_right(l, y=1):
    if len(l) <= 1:
        return l
    y = -y % len(l)
    return l[y:] + l[:y]


# print(rotate_right(l, 19))


my_l = [x for x in range(1, 15)]
print([x for x in range(1, 15)])
print(rotate_right(my_l, 3))
print(rotate_right(my_l, 6))
print(rotate_right(my_l, 9))
print(rotate_right(my_l, 12))



