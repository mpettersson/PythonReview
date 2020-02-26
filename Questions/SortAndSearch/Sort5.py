"""
    SORT5

    Suppose you are given a set S of 25 distinct integers and a CPU that has a special instruction, sort5, that can sort
    five ints in one cycle.  Your task is to identify the largest, second-largest, and third-largest integers in S using
    sort5 to compare and sort subsets of S; furthermore, you must minimize the number of calls to sort5.

    Note: Other variations of this problem include 25 horses or 25 cyclist and ask for the minimum number of five
    horse/person races to find the fastest, second fastest, and third fastest horse/person.

    Example:
        input = [390, 334, 233, 439, 377, 516, 170, 379, 620, 997, 53, 813, 285, 501, 96, 586, 847, 347, 436, 883, 898,
                129, 353, 346, 269]
        output = [997, 898, 883], 7  # where 7 is the number of calls to sort5

    This question is from Elements of Programming Interviews; SEE https://elementsofprogramminginterviews.com/.
"""


def sort5(l):
    return sorted(l, reverse=True)


def three_largest_of_twenty_five_using_sort5(l):
    num_sort5_calls = 0
    five_subsets_results = []

    # Using sort5, sort subsets of five:
    for i in range(0, 25, 5):
        five_subsets_results.append(sort5(l[i:i+5]))
        num_sort5_calls += 1

    # Using sort5 a 6th time on the largest values from the previous 5 calls, we will know:
    #   - What number is the overall largest.
    #   - The three subsets containing the only possible second and third largest numbers.
    sixth_sort5_call_results = sort5([five_subsets_results[i][0] for i in range(5)])
    num_sort5_calls += 1

    # The next five numbers to sort with sort5 are:
    #   - The next TWO largest numbers in the subset with the overall largest number.
    #   - The TWO largest numbers from the subset that came in second largest (in the 6th sort5 call).
    #   - The THIRD largest value from the 6th sort5 call.
    last_subset_to_sort = []
    for subset in five_subsets_results:
        if sixth_sort5_call_results[0] in subset:
            last_subset_to_sort += subset[1:3]
        elif sixth_sort5_call_results[1] in subset:
            last_subset_to_sort += subset[0:2]
    last_subset_to_sort.append(sixth_sort5_call_results[2])

    # The 7th and last sort5 call will order the second and third largest values:
    seventh_sort5_call_results = sort5(last_subset_to_sort)
    num_sort5_calls += 1

    return [sixth_sort5_call_results[0], seventh_sort5_call_results[0], seventh_sort5_call_results[1]], num_sort5_calls


l = [390, 334, 233, 439, 377, 516, 170, 379, 620, 997, 53, 813, 285, 501, 96, 586, 847, 347, 436, 883, 898, 129, 353,
     346, 269]
print("l:", l)
print()

print("three_largest_of_twenty_five_using_sort5(l):", three_largest_of_twenty_five_using_sort5(l))


