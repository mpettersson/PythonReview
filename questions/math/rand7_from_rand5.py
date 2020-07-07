"""
    RAND7 FROM RAND5

    Implement a method rand7() given rand5().  That is, given a method that generates a random number between 0 and 4
    (inclusive), write a method that generates a random number between 0 and 6 (inclusive).
"""
import random


# The given rand5 method:
def rand5():
    return random.randint(0, 5)


# NOTE: The solution is non-deterministic because we don't know how many times we'll call rand5.
def rand7():
    while True:
        num = 5 * rand5() + rand5()  # 5 * rand5() = 0, 5, 10, 15, 20 and rand5() = 0, 1, 2, 3, 4 so 0-24 with same prob
        if num < 21:  # If we included 21-24, the mod results prob wouldn't be uniform (0-3 would have higher prob).
            return num % 7


print("rand7():", rand7())

sum = 0
iterations = 2000
for _ in range(iterations):
    sum += rand7()
print(f"The average of rand7's results (of {iterations} iterations) is {sum/iterations}.")




