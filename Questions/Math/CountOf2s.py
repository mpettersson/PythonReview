"""
    COUNT OF 2S

    Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive).

    Example:
        input = 25
        output = 9 (2, 12, 20, 21, 22, 23, 24, and 25--Note that 22 counts for two 2s)
"""
import time


# Approach 1: Brute Force
def count_twos_brute_force(num):
    count = 0
    for i in range(1, num + 1):
        while i > 0:
            if (i % 10) == 2:
                count += 1
            i = i // 10
    return count


# Approach 2: Optimal--Count the ratios (percent) of twos for each digit in the number.
# Has three individual cases: digit < 2, digit == 2, digit > 2.
def count_twos(num):
    count = 0
    for d in range(0, len(str(num))):
        count += count_twos_at_position(num, d)
    return count


def count_twos_at_position(num, digit):
    power_of_10 = 10 ** digit
    next_power_of_10 = power_of_10 * 10
    right = num % power_of_10

    round_down = num - num % next_power_of_10
    round_up = round_down + next_power_of_10

    digit = (num // power_of_10) % 10
    if digit < 2:  # Case One: digit < 2
        return round_down // 10
    elif digit == 2:  # Case Two: Digit == 2
        return round_down // 10 + right + 1
    else:  # Case Three: Digit > 2
        return round_up // 10


small_num = 25
large_num = 961325
print("small_num:", small_num)
print("large_num:", large_num)
print()

print("count_twos_brute_force(", small_num, "):", count_twos_brute_force(small_num))
t = time.time()
print("count_twos_brute_force(", large_num, "):", count_twos_brute_force(large_num), "(Took", time.time() - t, "seconds.)")
print()

print("count_twos(", small_num, "):", count_twos(small_num))
t = time.time()
print("count_twos(", large_num, "):", count_twos(large_num), "(Took", time.time() - t, "seconds.)")




