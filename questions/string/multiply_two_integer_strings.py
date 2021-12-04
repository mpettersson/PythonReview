"""
    MULTIPLY TWO INTEGER STRINGS (leetcode.com/problems/multiply-strings)

    Write a function which accepts two non-negative integer strings (consisting of character digits '0' to' 9') and
    returns a string of their product (without directly converting to integers).

    Example:
        Input = '123', '456'
        Output = '56088'

"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - Can the strings have leading zeros (other than a actual zero value)?
#   - What are the estimated lengths of the strings (empty string)?
#   - Negative values, zero value?


# APPROACH: Iterative
#
# This approach is similar to the traditional multiplication method as taught in elementary school (just in case you
# forgot, the following is an example); only the steps have been broken down to better fit our iterative loops.
#
#  (Traditional Multiplication:)
#
#                 1  2  3
#              x  4  5  6
#             ------------
#                 7  3  8
#              6  1  5
#        +  4  9  2
#       ------------------
#           5  6  0  8  8
#
# NOTE: The key observations for this question are:
#           1) We know the MAX size of a result (given the lengths of the two operands).
#           2) Order (of two single digit multiplications) doesn't matter.
#           3) The positions of the single digits (and their product in the result list) is known.
#
# First we create a result list, filled with zeros, of the maximum length that the result could be (given two numbers of
# set lengths).  Then a single loop over one number's digits, with a single nested loop over the other number's digits
# will be all that is needed to compute the product.  For each pair of digits (where one digit is from the first string
# and the second digit is from the second string) simply (convert to integers,) multiply and (immediately) merging the
# result into the result list (or the list that accumulates the sum of all of the products).  Once all single digits
# have been multiplied, remove any leading zeros from the list, then convert the digits to character digits, join the
# list into a single string, and return.
#
# For example, to multiply 123 and 456, the following is the state of the list and the single digit multiplications:
#
#           1  2  3
#        x  4  5  6
#       ------------
#
#       Initial l:   [0, 0, 0, 0, 0, 0]
#
#       l after 3*6: [0, 0, 0, 0, 1, 8]     (or a[2] * b[2])
#       l after 3*5: [0, 0, 0, 1, 6, 8]     (or a[2] * b[1])
#       l after 3*4: [0, 0, 1, 3, 6, 8]     (or a[2] * b[0])
#
#       l after 2*6: [0, 0, 1, 4, 8, 8]     (or a[1] * b[2])
#       l after 2*5: [0, 0, 2, 4, 8, 8]     (or a[1] * b[1])
#       l after 2*4: [0, 1, 0, 4, 8, 8]     (or a[1] * b[0])
#
#       l after 1*6: [0, 1, 1, 0, 8, 8]     (or a[0] * b[2])
#       l after 1*5: [0, 1, 6, 0, 8, 8]     (or a[0] * b[1])
#       l after 1*4: [0, 5, 6, 0, 8, 8]     (or a[0] * b[0])
#
#       Final l:     [0, 5, 6, 0, 8, 8] ==> [5, 6, 0, 8, 8] ==> "56088"
#
# Time Complexity: O(m*n), where m and n are the lengths of the strings a and b.
# Space Complexity: O(m+n), where m and n are the lengths of the strings a and b.
def multiply_two_integer_strings(a, b):
    if a == '0' or b == '0':
        return '0'
    m = len(a)
    n = len(b)
    l = [0] * (m + n)                                   # l = Cumulative product sum (each index is a pow of 10).
    for i in range(m-1, -1, -1):                        # Digits indices in a.
        for j in range(n-1, -1, -1):                    # Digits indices in b.
            temp = (int(a[i]) * int(b[j])) + l[i+j+1]   # temp = prod of a[i] and b[j] PLUS the previous remainder!
            l[i+j] += temp // 10                        # Add the carry to the previous remainder.
            l[i+j+1] = temp % 10                        # Update the remainder.
    while not l[0]:                                     # Pop off any leading zeros.
        l.pop(0)
    return ''.join([str(e) for e in l])


# APPROACH: Iterative
#
# This is a slightly altered/refactored version of the approach above.
#
# Time Complexity: O(m*n), where m and n are the lengths of the strings a and b.
# Space Complexity: O(m+n), where m and n are the lengths of the strings a and b.
def multiply_two_integer_strings_alt(a, b):
    if a == '0' or b == '0':
        return '0'
    l = [0] * (len(a) + len(b))
    for i in reversed(range(len(a))):
        for j in reversed(range(len(b))):
            l[i+j+1] += int(a[i]) * int(b[j])
            l[i+j] += l[i + j + 1] // 10
            l[i+j+1] %= 10
    while not l[0]:                             # While there is a leading zero:
        l.pop(0)                                    # Pop it off.
    return ''.join([str(e) for e in l])         # Convert to strings, then join, and return.


args = [('123', '456'),
        ('10000', '10000'),
        ('9', '9'),
        ('123', '0'),
        ('0', '123'),
        ('0', '0'),
        ('11111', '111111')]
fns = [multiply_two_integer_strings,
       multiply_two_integer_strings_alt]

for a, b in args:
    for fn in fns:
        print(f"{fn.__name__}({a!r}, {b!r}): {fn(a, b)!r}")
    print()


