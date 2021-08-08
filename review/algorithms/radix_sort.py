"""
    RADIX SORT

    Average Runtime:    O(kn), where n is the number of elements and k is the number of passes (number of radix).
    Worst Runtime:      O(kn)
    Best Runtime:       O(kn)
    Space Complexity:   O(kn)
    Alg. Paradigm:      Non-Comparative Integer Sorting 
    Sorting In Place:   No
    Stable:             Yes     (the default alg changes the relative order of elements with equal keys)
    Online:             No      (can sort a list as it receives it)

    TODO DESCRIPTION
"""


# A function to do counting sort of l according to the digit represented by exp.
def counting_sort(l, digit_pos):
    n = len(l)
    output = [0] * n                            # The output list elements that will have sorted l.
    count = [0] * 10

    for i in range(n):                          # Store count of occurrences in count.
        index = l[i] // digit_pos
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]                # count[i] now contains actual position of this digit in output.

    i = n - 1
    while i >= 0:                               # Build the output list.
        index = l[i] // digit_pos
        output[count[index % 10] - 1] = l[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(l)):
        l[i] = output[i]                        # Update l with sorted values.


def radix_sort(l):
    l_max = max(l)

    # Note that instead of passing digit number, exp is passed. exp is 10^i where i is current digit number
    exp = 1
    while l_max / exp > 0:
        counting_sort(l, exp)
        exp *= 10


# def get_digit(number, digit):
#     return number // 10**digit % 10
#
#
# # Needed for the Count Sort inside the Radix
# def prefix_sum(to_calc=None):
#     if to_calc is None:
#         to_calc = []
#     for i in range(1, len(to_calc)):
#         to_calc[i] += to_calc[i - 1]
#     return to_calc
#
#
# def radix(l, counter=0):
#     tempList = [None] * len(l)
#     counts = [0] * 10                   # Used to store numbers from 0, 9
#     # for all the numbers, get the int[counter] and add to counts[]
#     #   i.e. 231[1] = 3
#     for c in l:
#         counts[get_digit(c, counter)] += 1
#     prefix_sum(counts)
#     # Rearrange unsortedList to tempList
#     for it in reversed(l):
#         counts[get_digit(it, counter)] -= 1
#         tempList[counts[get_digit(it, counter)]] = it
#
#     # If the amount of itterations is < the largest digit length in the list Run a pass on sorting the list again
#     if counter < len(str(max(l))):
#         return radix(tempList, counter + 1)
#     else:
#         return l


from math import log10
from random import randint

def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

# l = [ randint(1, 99999) for x in range(100) ]
# sorted = radixsort(l)
# print sorted


l = [170, 45, 2, 75, 90, 802, 24, 2, 66, 0, -1]

(lambda y: (print(f"radix_sort({y}): ", end=""), radix_sort(y), print(y, "\n")))((lambda x: x[:])(l))

(lambda y: (print(f"radixSort({y}): ", end=""), radixSort(y), print(y, "\n")))((lambda x: x[:])(l))

