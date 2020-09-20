"""
    MISSING INT (CCI 10.7)

    Given an input file with four billion non-negative integers, provide an algorithm to generate an integer that is not
    contained in the file.  Assume you have 1 GB of memory available for this task.

    Variation:
        What if you have only 10 MB of memory?  Assume that all the values are distinct and we now have no more than one
        billion non-negative integers.
"""
import os


# Observations:
#   The file size is 16 GB (4,000,000,000 * 4B = 16GB), so can't read it all into memory.
#
#   The file has (signed, NOT unsigned,) 'non-negative integers'.  This is important because an int is 4B, or 32b, which
#   allows for 4,294,967,296 binary combinations (or values). (Signed) Ints use the combinations for a value range of
#   [–2,147,483,648, 2,147,483,647], therefore, there must be 4,294,967,296 - 2,147,483,648 duplicates.
#
#   We can use 1GB memory, or 8,589,934,592b, so we have enough bits to enumerate each of the values.


# Wrong Approach: REMEMBER, if you use ints as bit vectors, DIVIDE by 32!!!  The bit_vector below uses 2.5 GB of memory.
# Time and space complexity of this approach is O(n) where n is the length of the file.
def missing_int_wrong(file_name):
    if file_name is not None and os.path.isfile(file_name):
        num_32_bit_positive_ints = 2 ** 31
        bit_vector = [0] * num_32_bit_positive_ints
        with open(file_name, mode='rb') as f:
            line = f.readline()
            while line:
                bit_vector[int(line)] = 1
                line = f.readline()
        for i in range(num_32_bit_positive_ints):
            if bit_vector[i] is 0:
                return i


# Int Bit Vector Approach:  Better, however, the byte_array below uses 512 MB of memory.  Time and space complexity of
# this approach is O(n) where n is the length of the file.
def missing_int_via_int_bit_vector(file_name):
    if file_name is not None and os.path.isfile(file_name):
        num_32_bit_positive_ints = 2 ** 31
        bit_vector = [0] * (num_32_bit_positive_ints // 32)
        with open(file_name, mode='rb') as f:
            line = f.readline()
            while line:
                n = int(line)
                bit_vector[n//32] |= 1 << (n % 32)
                line = f.readline()
        for i in range(len(bit_vector)):
            for j in range(32):
                if bit_vector[i] & (1 << j) == 0:
                    return i * 32 + j


# Bytearray Approach:  Unlike many other types in python, each element of a bytearray takes exactly one byte; therefore
# the byte_array below uses 256 MB of memory.  Time and space complexity of this approach is O(n) where n is the length
# of the file.
def missing_int(file_name):
    if file_name is not None and os.path.isfile(file_name):
        num_32_bit_positive_ints = 2 ** 31
        byte_array = bytearray(num_32_bit_positive_ints // 8)
        with open(file_name, mode='rb') as f:
            line = f.readline()
            while line:
                n = int(line)
                byte_array[n//8] |= 1 << (n % 8)
                line = f.readline()
        for i in range(len(byte_array)):
            for j in range(8):
                if byte_array[i] & (1 << j) == 0:
                    return i * 8 + j


# Variation (With Limit) Bytearray Approach:
# The constraint of 10MB is equivalent to 2**23B.  That means the bytearray can hold max 2**21 items (because each
# element is an int and takes up 4B).  The number of bytearray items/partitions
def missing_int_w_limit(file_name, byte_limit=2 ** 23):
    if file_name is not None and os.path.isfile(file_name):
        num_lines = 0
        with open(file_name, mode='rb') as f:
            line = f.readline()
            while line:                                                 # Get line count
                line = f.readline()
                num_lines += 1
            f.seek(0, 0)
            max_byte_array_len = byte_limit // 4                        # Upper bound for bytearray length.
            range_size = 1
            while 10 * range_size < max_byte_array_len:                 # Get a range_size that'll fit in the bytearray
                range_size *= 10
            min_byte_array_len = range_size // 8
            if min_byte_array_len < range_size < max_byte_array_len:    # Validate range_size
                count_list = [0] * ((num_lines // range_size) + 1)
                line = f.readline()
                while line:                                             # Count number of values in each range
                    count_list[int(line)//range_size] += 1
                    line = f.readline()
                f.seek(0, 0)
                range_missing_num = count_list.index(min(count_list))   # The range index with the missing value.
                byte_array = bytearray(range_size//8)
                line = f.readline()
                while line:                                             # Last time reading the numbers...
                    n = int(line)
                    if n // range_size == range_missing_num:            # Populate the bitvector/bytearray
                        n -= (range_size * range_missing_num)
                        byte_array[n // 8] |= 1 << (n % 8)
                    line = f.readline()
                for i in range(len(byte_array)):                        # Get the value from the bitvector/bytearray.
                    for j in range(8):
                        if byte_array[i] & (1 << j) == 0:
                            return (i * 8 + j) + (range_missing_num * range_size)
            else:
                print("Byte limit too low...")


