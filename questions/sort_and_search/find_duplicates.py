"""
    FIND DUPLICATES (CCI 10.8)

    You have an array with all the numbers from 0 to n, where n is less than 32000.  The list may have duplicate entries
    and you do not know what n is.  With only 4 KB of memory available, how would you print all duplicate elements in
    the list.
"""
import os
import random


# Bytearray Approach:
def find_duplicates(file_name):
    if file_name is not None and os.path.isfile(file_name):
        byte_arr = bytearray(4000)
        with open(file_name, mode='rb') as f:
            line = f.readline()
            while line:
                n = int(line)
                if byte_arr[n // 8] & 1 << (n % 8):
                    print(n)
                else:
                    byte_arr[n // 8] |= 1 << (n % 8)
                line = f.readline()


# IntBitVector Approach:
def find_duplicates_int_bit_vector(file_name):
    bit_vector = IntBitVector(32000)
    with open(file_name, mode='rb') as f:
        line = f.readline()
        while line:
            n = int(line)
            if bit_vector.get(n):
                print(n)
            else:
                bit_vector.set(n)
            line = f.readline()


class IntBitVector:
    def __init__(self, size):
        self.byte_arr = [0 for _ in range((size >> 5) + 1)]

    def get(self, pos):
        return self.byte_arr[pos >> 5] & (1 << (pos % 32)) != 0

    def set(self, pos):
        self.byte_arr[pos >> 5] |= 1 << (pos % 32)


# Helper Functions:
def create_file(file):
    l = [i for i in range(32000)]
    random.shuffle(l)
    l[random.randint(0, 32000)] = 0
    l[random.randint(0, 32000)] = 420
    with open(file, mode='w') as f:
        for i in l:
            f.write(str(i) + '\n')


def remove_file(file):
    if file is not None and os.path.isfile(file):
        os.remove(file)


file = 'find_duplicates.txt'
print(f"create_file({file})")
create_file(file)

print(f"\nfind_duplicates({file})")
find_duplicates(file)

print(f"\nfind_duplicates_int_bit_vector({file})")
find_duplicates_int_bit_vector(file)

print(f"\nremove_file({file})")
remove_file(file)


