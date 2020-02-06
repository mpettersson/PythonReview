import math
import random
from functools import reduce

# Single line comment

''' 
    Multi line comment
'''

"""
    Multi line Comment 
"""


"""
NAMING CONVENTIONS

Packages & Modules
    - All lowercase.
    - Try and use one word.
    - If multiple words are needed, separate them with an underscore.


Classes
    - UpperCaseCamelCase
    - NOTE: Python’s built-in classes are usually lowercase words.

 
Functions & Global Variables
    - All lowercase.
    - Separate words with underscores.


Methods & Instance Variables
    - all lowercase.
    - Separate words with underscores.
    - Non-public instance variables should begin with a single underscore
    - If an instance name needs to be mangled, two underscores may begin its name


Constants
    - ALL UPPERCASE
    - Separate words with underscores.
    
"""

print("Hello World")
print('Hello World')


# name = input("What is your name ")
# print("Hi", name)

# Possible assignments, but things you probably won't want to do:
v1 = 3; v2 = "String"
print(v1, v2)
v1 = v2 = 4
print(v1, v2)

# REMEMBER, data is DYNAMICALLY TYPED in python (and all data is an object) so this is legal:
a = 1
a = "string"

# To determine the type of a variable use 'type()'
print(type(a))

# Complex numbers are made up of REAL + IMAGINARY parts
imag_num = 5 + 6j

# Booleans are either True or False
bool_true = True
bool_false = False

# Use isinstance(object, type) to verify a type:
print(isinstance(bool_false, bool))


###########
# STRINGS #
###########

# Are IMMUTABLE

str_single_quotes = 'blah \n blah \' " '
str_double_quotes = "blah \n blah ' "

# Raw String (ignores escape sequences)
str_raw = r"Escape sequences will be ignored \n"

# String (or statement) over multiple lines:
str_one = """This WILL have
            new lines and tabs
            in it..."""
print(str_one)

str_two = ('This will '
           'not have '
           'newlines in it')
print(str_two)

str_three = 'This, too, will' \
            ' not have new lines' \
            'in it.'

print(str_three)

string_var = "Hello World!!!"

# Common String Operations
print("Length (len()):", len(str_three))
print("Replace substrings with string_var.replace(\"world\", \"WORLD\"):", string_var.replace("world", "WORLD"))
print("Get first index with string_var[0]:", string_var[0])
print("Get last index with string_var[-1]:", string_var[-1])
print("Get first three with string_var[0:3]:", string_var[0:3])
print("Get every other with string_var[0:-1:2]:", string_var[0:-1:2])
print("Check if a string has a substring with ('Hell' in string_var)", ("Hell" in string_var))
print("     Stripped whitespace from ends    ".strip())     # aka trim() in Java
print("     Stripped whitespace from left    ".lstrip())
print("     Stripped whitespace from right    ".rstrip())
print("string_var.upper():", string_var.upper())
print("string_var.lower():", string_var.lower())
print("Check alphaNumeric string with AString123.isalnum():", "AString123".isalnum())
print("Check alpha string with AString.isalnum():", "AString".isalpha())
print("Check numeric string with 123.isalnum():", "123".isdigit())

# Note you CANT reassign an index of a string, i.e., this won't work:
# string_var[6] = w
# But you can do this:
string_var = string_var[:6] + "w" + string_var[7:]
# or you could do this:
string_var = string_var.replace("world", "World")


# List of words (strings) to string
var_list = ["A", "List", "Of", "Words"]
var_string_from_list = " ".join(var_list)
print(var_string_from_list)

# String to a list of words (strings)
print(var_string_from_list.split(" "))

# SORT STRING - There isn't one function to sort a string, in stead, you need to do this:
print("To sort strings use \"\".join(sorted(string_var)):", "".join(sorted(string_var)))

# Remove whitespace (including \t and \n) from a string, do this:
whitespace_str = "   \t no m o r r \n whitespace      "
print("To remove whitespaces, \\n, and \\t use \"\".join(whitespace_str.split()):", "".join(whitespace_str.split()))


int_one = ( 1 + 2
            + 3 )
print(int_one)


# Casting to types
print("Cast", int(5.4), type(int(5.4)))
print("Cast", str(5.4), type(str(5.4)))
print("Cast", chr(97), type(chr(97)))
print("Cast", ord('a'), type(ord('a')))


# Printing/Output
print(4, 1, 1982, sep='/')
print("How to print without a trailing newline (use end='').", end='')

# Printing with formatting using the %:
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))

# Formatting with the .format method.
x1 = 1; x2 = 5; x3 = 10
print('{0:2d} {1:3d} {2:4d}'.format(x1, x1*x1, x1*x1*x1))
print('{0:2d} {1:3d} {2:4d}'.format(x2, x2*x2, x2*x2*x2))
print('{0:2d} {1:3d} {2:4d}'.format(x3, x3*x3, x3*x3*x3))

# Simple Math
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)  # EXP
print("5 // 2 =", 5 // 2)  # INT DIV

# No ++ operation but can do:
int_one += 1


# fstring or "formatted string literals" Notes:
#   Added in Python 3.6
#   String with a f or F at the beginning and {} that expressions to be replaced with values at run time.
print(f"{int_one} + {int_one} = {int_one + int_one}")
import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

# infinity, or inf
print(math.inf > 0)

# Not a Number or nan
print(math.inf - math.inf)

# How to print binary with python functions
print("bin(37): ", bin(37))                         # This includes the 0b prefix.
print("\"{0:b}\".format(37)", "{0:b}".format(37))   # This does NOT include the 0b prefix.



#########################
# Conditional Operators #
#########################

age = 12
if age < 5:
    print("Too young for school.")
elif (age >= 5) and (age <= 6):
    print("Go to Kindergarten")
elif age > 6 and age <= 17:
    print("Go to grade", (age - 5))
else:
    print("Go to college...")

# Terinary conditional:
terinary_result = True if random.randint(1, 101) < 50 else False
terinary_result = 42 if random.randint(1, 101) < 50 else 69


#####################
# BITWISE OPERATORS #
#####################

print("Enter integers as binary with the 0b or 0B prefix, i.e., 0B1010 is ", 0B1010)
print("Enter negative integers as binary with the -0b or -0B prefix, i.e., -0B1010 is ", -0B1010)


#   &  - Binary AND	Operator copies a bit to the result if it exists in both operands
#   |  - Binary OR	It copies a bit if it exists in either operand.
#   ^  - Binary XOR	It copies the bit if it is set in one operand but not both.
#   ~  - Binary Ones Complement	It is unary and has the effect of 'flipping' bits.
#   <<  - Binary Left Shift	The left operands value is moved left by the number of bits specified by the right operand.
#   >>  - Binary Right Shift: The left operands value is moved right by the num of bits specified by the right operand.

# 60 = 0011 1100
# 13 = 0000 1101

# 60 & 13 == 0011 1100 & 0000 1101 -> 12 == 0000 1100
print("Binary AND: 60 & 13 = ", 60 & 13)

# 60 | 13 == 0011 1100 | 0000 1101 -> 61 == 0011 1101
print("Binary OR: 60 | 13 = ", 60 | 13)

# 60 ^ 13 == 0011 1100 ^ 000 1101 -> 49 == 0011 0001
print("Binary XOR: 60 ^ 13 = ", 60 ^ 13)

# ~60 == ~0011 1100 -> -61 == 1100 0011
print("Binary Ones Complement: ~60 = ", ~60)

# 60 << 2 == 0011 1100 << 0000 0010 -> 1111 0000 == 240
print("Binary Left Shift: 60 << 2 = ", 60 << 2)

# 60 >> 2 ==  0011 1100 >> 0000 0010 -> 0000 1111 == 15
print("Binary Right Shift: 60 >> 2 = ", 60 >> 2)


#########
# LISTS #
#########

# MUTABLE,
# CAN contain different types,
# ARE UN-Hashable.


list_var = [1, 3.14, "Matt", True]


# Common List Operations
print("Get length with len(list_var):", len(list_var))
print("Get first item with list_var[0]:", list_var[0])
print("Get last item with list_var[-1]:", list_var[-1])
# Can update or reassign with list (bc they're mutable)
list_var[0] = 0

print(list_var)
list_var[2:4] = ["Bob", False]
print(list_var)
# Insert one thing (HAS TO BE IN LIST)
list_var[2:2] = ["Brenton"]
print(list_var)
# Insert two things (HAS TO BE IN LIST)
list_var[2:2] = [89, 90]
print(list_var)
# actual insert method (DON'T PUT IN LIST)
list_var.insert(2, "inserted string")
print(list_var)
# How to add a list to the end of another list
list_var = list_var + ["Adding", "To", "End"]
# How to remove a specific value
list_var.remove("Brenton")
list_var.pop(0)
print(list_var)
# How to add a list to the beginning of the list:
list_var = [12.44, 55.55] + list_var
# How to check membership (if something is in a list)
print("Check if a value is in a list with 3.14 in list_var:", 3.14 in list_var)
print("Get the min value (where all the values are the same type) of a list with min([1,2,3]):", min([1,2,3]))
print("Get the max value (where all the values are the same type) of a list with max([1,2,3]):", max([1,2,3]))
print("Reverse a list with list_var[::-1]:", list_var[::-1])
print("How to make a list with range using list(range(0, 10)):", list(range(0, 10)))


#########
# LOOPS #
#########

# NOTE: No DO WHILE loops, just use a while True with a break!
# NOTE: No C STYLE FOR loop, if you can define a counter before the loop or use for i, item in enumerate(iterable):

w1 = 1
while w1 < 5:
    print(w1, " ", end="")
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2, " ", end="")
    elif w2 == 9:
        break
    else:
        w2 += 1
        continue
    w2 += 1

# Enumerate Example
a_list_of_things = [1, 3.14, "hello"]
for i, v in enumerate(a_list_of_things):
    print(i, v, end="")


for x in range(0, 10):
    print(x, " ", end="")
print()

for x in list_var:
    print(x, " ", end="")
print()

print(list(range(0, 10)))


##########
# TUPLES #
##########

# IMMUTABLE,
# CAN have different types,
# CAN have duplicates
# ARE Hashable.

tup_var = (1, 3.14, "Matt", "Matt")

print("Get the length of a tuple with len(tup_var):", len(tup_var))
print("Get the 1st item of a tuple with tup_var[0]", tup_var[0])
print("Get the last item of a tuple with tup_var[-1]", tup_var[-1])
print("Get the first two items of a tuple (as a tuple) with tup_var[0:2]", tup_var[0:2])
print("Get every other items of a tuple (as a tuple) with tup_var[0:-1:2]", tup_var[0:-1:2])
print("Reverse a tuple with tup_var[::-1]", tup_var[::-1])

# REMEMBER: Tuples are IMMUTABLE, so no reassignment:
# tup_var[0] = 0 # Will Raise TypeError.


##############
# DICTIONARY #
##############

# MUTABLE,
# CAN'T have duplicates,
# CAN have mixed types,
# ARE UN-Hashable,
# CAN'T use LIST/DICT/SET (un-hashable types) as KEY.


dict_var = {
    "key": "will get replaced with value",
    "key": "value", # This will update, or replace, the first value supplied...
    "Key": "Value",
    "name": "Matt",
    "age": 37,
    "key two": "value two",
    " key three": " value three",
    "k4": "v4",
    "k": 4,
    4: 5,
    3.1415: "pi"
}

# NOTE that order is not maintained pre 3.6 in dict.
print(dict_var)


# NOTE You can use the dict constructor to cast a list of two-value tuples as a dictionary.
dict_var_two = dict([
    ("Key One", "value one"),
    ("Key Two", "value two")
])


print("Get dict length with len(dict_var)", len(dict_var))
print("Get value of a key in a dict with dict_var[key]", dict_var["key"])
print("Assign a key:value to a dict with dict_var[new_key]:new_value"); dict_var["new_key"] = "new_value"
print("Reassign a value to a key in a dict with dict_var[key]:new_value"); dict_var["key"] = "new_value"
print("List the keys of a dict with dict_var.keys():", dict_var.keys())
print("List the values of a dict with dict_var.values():", dict_var.values())
print("List the keys and values of a dict with dict_var.items():", dict_var.items())
print("List as tuples the keys and values of a dict with list(dict_var.items()):", list(dict_var.items()))
print("Delete the a key and value in a dict with del dict_var[new_key]"); del dict_var["new_key"]
print("Pop a key, returning a value, in a dict with dict_var.pop(Key)", dict_var.pop("Key"))

# How to iterate over keys in a dict:
for k in dict_var:
    print(k, " ", end="")

# How to iterate over values in a dict:
for v in dict_var.values():
    print(v, " ", end="")

# How to iterate over keys and values in a dict:
for k, v in dict_var.items():
    print(k, v, " ", end="")


# Formatted printing with dictionary mapping:
print("\n%(name)s age is %(age)d" % dict_var)


########
# SETS #
########
# An UNORDERED list,
# Has UNIQUE value,
# CAN add/remove values,
# CAN'T update values (values are immutable),
# Un-hashable.

# SET OPERATIONS
#   -   Difference
#   |   Union
#   &   Intersection
#   ^   Symmetric Difference

# NOTE: Can use frozenset() to make a set immutable therefore allowing it to be used in other sets or hash-based ops.

# Can create a populated set with curly brackets or set(<list>).
set_var = {"Matt", "Value", 1, 1, 3.14}   # Duplicates don't cause errors, but will only be included once in the set.
set_var_two = set(["Matt", 1, 3.14, "Hello World", 42])

# NOTE: CANNOT create empty set with curly brackets {}.

# NOTE: Sets don't support item assignment, i.e., the next line would cause a TypeError:
# set_var[0] = "new string"

print("set_var = ", set_var)

print("Get the length of a set with len(set_var)", len(set_var))
print("Add a value to a set with set_var.add(value):"); set_var.add("value")
print("Remove a value from a set with set_var.discard(value):", set_var.discard("value"))
print("Pop a random value from a set with set_var.pop():", set_var.pop())
print("Return common values of two sets with set_var.intersection(set_var_two):", set_var.intersection(set_var_two))
print(set_var.symmetric_difference(set_var_two))
print(set_var.difference(set_var_two))
print("Add (join) to a set with set_var |= {99}"); set_var |= {99, 101}
print("Join, or combine, sets with set_var_three = set_var | set_var_two"); set_var_three = set_var | set_var_two
print("Clear all items in a set with set_var_three.clear():", set_var_three.clear())

# NOTE: To create a set that cant be changed use frozenset:
frz_set_one = frozenset({"frozen", "set"})
frz_set_two = frozenset(["frozen", "set"])


########
# SORT #
########

# SORT()
# List ONLY method, sorts in place, returns None, faster than sorted() because it doesn't create a new list.

# SORTED()
# Works on ANY ITERABLE (strings, tuples, dicts, and generators), returns a list. A sorted dict returns the KEYS.

tup_list = [(65, "s", 100), (70, "d", 150), (56, "l", 90), (70, "f", 190), (60, "k", 95), (68, "j", 110)]

# To sort on second item (position 1) of a tuple do this:
sorted(tup_list, key=lambda x: x[1])  # Remember this WILL NOT reassign tup_list, it'll just return a sorted list.
tup_list.sort(key=lambda x: x[1])  # Remember this WILL reassign tup_list to be sorted.
tup_list.sort(key=lambda x: (x[0], x[1]))  # This will sort first on the 0th item then on the 1st item.

# You can also use operator.itemgetter() to do the same thing:
import operator
tup_list.sort(key=operator.itemgetter(1))  # The same thing as above.
tup_list.sort(key=operator.itemgetter(0, 1))  # This will sort first on the 0th item then on the 1st item.

# How to sort a dictionary by VALUE (Python 3.6+):
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x_sorted_by_value = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

# How to sort a dictionary by KEY (Python 3.6+):
x_sorted_by_key = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}


#############
# FUNCTIONS #
#############

# Functions don't deal with Classes and their instance concept, Methods do, see Classes for methods.

# In Python, functions are the first class objects, that is:
#   Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
#   Functions can be defined inside another function and can also be passed as argument to another function.

# NONLOCAL
# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to
# the inner function.  See NESTED FUNCTION Example below for an example.

# FUNCTION ANNOTATIONS
# A syntax for adding arbitrary metadata annotations to Python functions:
def kinetic_energy(m: 'in KG', v: 'in M/S') -> 'Joules':
    return 1/2*m*v**2


# Can specify type with a function annotation, and can use default value
def add_two_ints(num1: int = 0, num2: int = 0):
    return num1 + num2


print(add_two_ints(3, 4))


# How to create a method with a variable number of arguments use '*args' in the def.
# NOTE: *args will then provide a TUPLE with the arguments provided.
def get_sum(*args):
    total = 0
    for x in args:
        total += x
    return total


print(get_sum(3, 5, 6, 7, 8, 11, 333))


# NOTE you can return multiple items/types.
def next_2(num):
    return num + 1, num + 2, "string"


i1, i2, s1 = next_2(5)
print(i1, i2, s1)


# A method that takes a function
def mult_list(list, func):
    for x in list:
        print(func(x), " ", end="")


# NESTED FUNCTION WITH NONLOCAL EXAMPLE:
def function_with_nested_function():
    x = "John"

    def nested_function():
        nonlocal x
        x = "hello"

    nested_function()
    return x


print(function_with_nested_function())


##########
# LAMBDA #
##########


# How to make an anonymous function via lambda:
def mult_mult_by(num):
    return lambda x: x * num


print("3 * 5 =", (mult_mult_by(3)(5)))

# MAP
one_to_4 = range(1, 5)
times2 = lambda x : x * 2
print("MAP: ", list(map(times2, one_to_4)))

# FILTER
print("FILTER:", list(filter((lambda x: x % 2 == 0), range(1, 11))))

# REDUCE
import functools
print("REDUCE", functools.reduce((lambda x, y: x + y), range(1, 6)))

# How to make a mult() function (like built-in sum()):
lambda_mult = lambda x:functools.reduce((lambda y,z:y*z), x)

# How to implement sum() with lambda:
lambda_sum = lambda *l: functools.reduce(lambda x, y: x + y, iter(l))
lambda_sum = lambda a=0, *b: functools.reduce((lambda x, y: x + y), iter(b))

# How to make a max() function (like built-in max())
lambda_max = lambda *l: functools.reduce(lambda a, b: a if a > b else b, iter(l))

# NOTE: If you want to pass around common operator functions (in lambdas or whatever), you can find them:
# import operator
# operator.sub
# operator.truediv
# operator.mul
# operator.add

# How to perform an operation (or operator function) on two operands.
def apply_op(left, op, right):
    return (lambda l, r, f: f(l, r))(left, right, op)


##############
# EXCEPTIONS #
##############

# Programs may name their own exceptions by creating a new exception class.

while False:
    try:
        number = int(input("Enter a number: "))
        break
    # How to except (catch) a ValueError (i.e., a specific error)
    except ValueError:
        print("Not a number!")
    # How to except (catch) any/all errors.
    except:
        print("Error occurred!")

# An example that uses the "as", "else", and "finally", keywords:
# The finally clause will execute as the last task before the try statement completes. The finally clause runs
# whether or not the try statement produces an exception.
# The else clause (which must follow all except clauses) is used for code that must be executed if the try clause
# does not raise an exception.
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except (ValueError, TypeError) as er:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise                   # This will raise the exception if the other two excepts didn't catch it.
else:
    print("The else clause (for a try) only get's printed if there was NO EXCEPTION")
    f.close()
finally:
    print("The finally cause always executes, exceptions or no exceptions!!!")

# How to raise an exception.
try:
    raise Exception('arg1', 'arg2')
except Exception as inst:
        print(type(inst))   # the exception instance
        print(inst.args)    # arguments stored in .args
        print(inst)         # __str__ allows args to be printed directly but may be overridden in exception subclasses
        x, y = inst.args    # unpack args
        print('x =', x)
        print('y =', y)


###############################
# RANDOM/SHUFFLE/SAMPLE NOTES #
###############################

# Need to import random:
import random

# Random float:  0.0 <= x < 1.0
random.random()

# Random float:  2.5 <= x < 10.0
random.uniform(2.5, 10.0)

# Random Integer:  0 to 9 inclusive
random.randrange(10)

# Random (Even) Integer from 0 to 100 inclusive:
random.randrange(0, 101, 2)

# Single random element from a sequence:
random.choice(['win', 'lose', 'draw'])

# SHUFFLE - Returns void, shuffles IN PLACE.
# To shuffle a list use random.shuffle():
int_list = [x for x in range(10)]
random.shuffle(int_list)  # Remember this will update the list with a shuffled list.

# To shuffle a string, you have to convert to list of char first, shuffle, then convert back:
name_str = "Matthew Charles Pettersson"
temp_list = list(name_str)
random.shuffle(temp_list)
name_str = ''.join(temp_list)

# Seeding the shuffle (to get repeatable shuffles):
random.seed(10)
rand_a = random.shuffle([x for x in range(10)])
random.seed(10)
rand_b = random.shuffle([x for x in range(10)])
print(rand_a == rand_b)  # True

# Shuffle two lists at once (maintaining same shuffle order) via zip:
int_list = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
chr_list = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
int_to_char_map = list(zip(int_list, chr_list))
random.shuffle(int_to_char_map)
int_list, chr_list = zip(*int_to_char_map)

# Shuffle dictionary keys:
ord_dict = {chr(i): i for i in range(97, 107)}
keys = list(ord_dict.keys())  # .keys() returns a type of dict_keys, so use list to make it a list type.
random.shuffle(keys)
shuffled_ord_dict = dict()
for key in keys:
    shuffled_ord_dict.update({key: ord_dict[key]})

# SAMPLE - Returns NEW LIST with the number of the sample size passed in.
# To sample a list use random.sample()
old_list = [x for x in range(10)]
new_list = random.sample(old_list, len(old_list))
new_sub_list = random.sample(old_list, len(old_list) // 2)


#######################
# ITERATOR & ITERABLE #
#######################

# ITERABLE
# An object capable of returning its members one at a time.
#
# Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict,
# file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that
# implements Sequence semantics.
#
# Not every Iterable is an Iterator (i.e., list IS iterable, but ISN'T a iterator).
#
#
# ITERATOR
# An object representing a stream of data.
#
# Repeated calls to the iterator’s __next__() method return successive items in the stream. When no more data are
# available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further
# calls to its __next__() method just raise StopIteration again.
#
# Iterators are required to have an __iter__() method that returns the iterator object itself so EVERY ITERATOR IS ALSO
# ITERABLE and may be used in most places where other iterables are accepted.
#
# To create an ITERATOR you only need to implement the __iter__() and __next__() methods.
# The __iter__() method returns the iterator object itself.
# And the __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls,
# it must raise StopIteration.

# The iter() function (which in turn calls the __iter__() method) returns an iterator.
# The next(iterator) will iterate through an iterators values.

# NOTE: Use next(iterator, default_value) as an alternative to a try/catch block.

iter_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(iter_list)

# iterate through it using next()
print(next(my_iter))
print(next(my_iter, None))  # Using default value to prevent StopIteration exception.
# next(my_iter) is same as my_iter.__next__()
print(my_iter.__next__())
print(my_iter.__next__())

# This will raise error, no items left
try:
    next(my_iter)
except StopIteration:
    print("StopIteration Error! (used next() too many times...)")


# Function that tests if an object is iterable:
def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


##################
# COMPREHENSIONS #
##################

# LIST COMPREHENSIONS
# Create a list of tuples from two lists:
int_list = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
chr_list = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
tl = [(i, j) for i, j in zip(int_list, chr_list)]

# Create a matrix:
matrix = [[0 for col in range(4)] for row in range(3)]

# Flatten a list of lists:
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]
flattened_list = [y for x in list_of_list for y in x]  # x == lists in list_of_list, y == each element in x.

# Flatten two lists:
f = [y for x in [int_list, chr_list] for y in x]  # Same as l = []; l.extend(int_list); l.extend(chr_list)
f = [y for x in zip(int_list, chr_list) for y in x]  # Same as [int_list[0], chr_list[0], ..., int_list[n], chr_list[n]]

# Comprehension with Conditionals:
cc = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]

# Comprehension with If-Else:
ifc = ["Even" if i % 2 == 0 else "Odd" for i in range(8)]

# Nested Comprehension (notice the order is backwards):
nc = [[i*j for j in range(1, 11)] for i in range(7, 9)]  # Same as for i in range(7,9): for j in range(1,11): i*j

# Complex Comprehension Example:
strings = [['foo', 'bar'], ['baz', 'taz'], ['x', 'var']]
cc = [(letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word) > 2 for letter in word]

# SET COMPREHENSIONS
# Same as list comprehension but with curly braces:
s = {x for x in int_list if x % 2 == 0}

# DICT COMPREHENSIONS
# Same as set comprehension but with colon and value:
d = {str(i): i for i in [0, 1, 2, 3, 4]}

# Switch key for value and value for key:
d = {value: key for key, value in d.items()}

# Remove a set of items from a dict:
s = {"1", "3"}
d = {key: d[key] for key in d.keys() - s}

# GENERATOR EXPRESSION (COMPREHENSIONS)
generator = (x for x in int_list if x % 2 == 0)

for x in generator:
    print(x, end="")
print()


##############
# GENERATORS #
##############

# Generator (Object):  An iterator of type generator.
# Generator FUNCTION: A function that returns a Generator Object. Use one or more YIELD statements.
# Generator EXPRESSION: A comprehension that allows you to create a generator object inline; uses parenthesis ().

# Generator Function that counts to infinity:
def count(start=0):
    num = start
    while True:
        yield num
        num += 1

# Generator Expression that counts to n:
n = 1000
ge = (x for x in range(n + 1))


###########
# FILE IO #
###########

import os

# How to create file if it does not exist:
if not os.path.exists('my_file.txt'):
    with open('my_file.txt', 'w'):
        pass

# Current working dir:
print("os.getcwd():", os.getcwd())

# Name of executing python script:
print("__file__:", __file__)

# How to find file path from dir root:
print(os.path.abspath("my_file.txt"))  # abspath DOES NOT dereference symbolic links! Just provides path from root.
print(os.path.realpath("my_file.txt"))  # realpath DOES derefence symbolic links!

# How to get directory name of a file:
print(os.path.dirname(os.path.realpath("my_file.txt")))  # Must use real/abs path.

# How to split directory/file name:
path, filename = os.path.split(os.path.realpath("my_file.txt"))  # Must use real/abs path.

# How to write (use mode="a" to append) to a file
with open("my_file.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some Random\nText, blah, blah, blah,\nLet's get schwifty baby!")

# The modes are:
#   r  - Open for reading plain text
#   w  - Open for writing plain text
#   a  - Open an existing file for appending plain text
#   rb - Open for reading binary data
#   wb - Open for writing binary data

# How to read from a file:
with open("my_file.txt", encoding="utf-8") as my_file:
    print(my_file.read())
    # my_file.readline() would just read one line.

"""
    with keyword notes

    with is used in exception handling to make the code cleaner and much more readable. 
    It simplifies the management of common resources like file streams. 
    
    Using "with open..." you don't need to close the connection/file (but doing so won't throw an error).

    To use with statement in user defined objects you only need to add the methods __enter__() and __exit__() 
    in the object methods.
"""

# How to close a file:
print(my_file.close())

# How to check if a file has been closed:
print(my_file.closed)

# How to delete a file:
try:
    os.remove("my_file.txt")
except OSError as e:  # if failed, report it back to the user ##
    print("Error: %s - %s." % (e.filename, e.strerror))


##########
# IMPORT #
##########

# How to import specific methods from a module.
from Review.PythonModule import factorial, print_hello_world
print(factorial(10))
print_hello_world()

# How to import all methods (that don't start with an underscore) from a module.
from PythonModule import *
print_foo_bar()
# REMEMBER: you can't do any of these:
#   print(_single_leading_underscore_variable)
#   _single_leading_underscore_function()
#   print(__double_leading_underscore_variable)
#   __double_leading_underscore_function()

# How to import a EVERYTHING
import PythonModule
print(PythonModule.factorial(10))
# Can use single and double leading underscore variables and functions:
print(PythonModule._single_leading_underscore_variable)
PythonModule._single_leading_underscore_function()
print(PythonModule.__double_leading_underscore_variable)
PythonModule.__double_leading_underscore_function()


#########
# CLASS #
#########

# CLASS VARIABLES
# All instance variables are defined in the init method.  Any variable defined outside init is a CLASS variable and
# will be shared by ALL instances.

# CLASS METHODS (not Functions)
# A method is implicitly passed the object on which it is invoked (via self).
# A method can operate on the data (instance variables) that is contained by the corresponding class
# A @classmethod decorated method has the class (not instance) passed as first arg (not self). Can be called without a
# class instance: MyClass.classmethod().
# A @staticmethod decorated method has neither the class, nor instance (self), passed as the first arg. These act like
# normal functions, but are grouped in, or associated with a class.

# SINGLE LEADING UNDERSCORE
# Methods and variables with single leading underscores indicate to other programmers that the method or variable is
# intended to be private. It is a weak "internal use" indicator, and does not prevent use of the method or variable.
#
# DOUBLE LEADING UNDERSCORES aka NAME MANGLING/SCRAMBLING
# Methods and variables with double leading underscores are used to ensure that subclasses don't accidentally override
# the private methods/vars of their superclasses. It's not designed to prevent deliberate access from outside.
#
# NOTE: from M import * does not import objects whose name starts with an underscore.

# DUNDER METHODS aka SPECIAL METHODS aka MAGIC METHODS
# Defined in Pythons data model documentation, these methods which begin and end with double underscores, are provided
# so a class can define its own behavior with respect to the language operators.
#   __init__    Class instance initializer (NOT constructor), python runtime provides constructor which calls __init__.
#   __del__     Class finalizer, called when the instance is about to be destroyed (not a destructor).
#   __new__     Called (before __init__) to create a new instance of a class, used for custom and immutable types.
#   __name__    Evaluates to __main__ or the actual module name depending on how the enclosing module is being used.
#   __repr__    Unambiguous output for devs; if not defined a default __class__.__name__ instance at id(self) is used.
#   __str__     Intended for readable end user output; if not defined print/str will use the result of __repr__.
#   __setitem__ Called to implement assignment to self[key] (only use if the object supports change to values for key).
#   __getitem__ Called to implement evaluation of self[key].
#   __getattr__ Only invoked if the attribute wasn't found in usual way. Good for implementing a fallback for missing
#               attributes, one way to provide lazy initialization. NOTE: __getattribute__ does the same but is invoked
#               before looking at the attributes; can easily cause infinite recursion.
#   __hash__    Called by built-in hash() function; for members of hashed collections should return an int.
#   __lt__      "Rich comparison" less than method; x<y will call x.__lt__(y)
#   __le__      "Rich comparison" less than or equal to method; x<=y will call x.__le__(y)
#   __eq__      "Rich comparison" equal to method; x==y will call x.__eq__(y)
#   __ne__      "Rich comparison" not equal to method; x!=y will call x.__ne__(y)
#   __gt__      "Rich comparison" greater than method; x>y will call x.__gt__(y)
#   __ge__      "Rich comparison" greater than or equal to method; x>=y will call x.__ge__(y)
#   __iter__    This method is called when an iterator is required for a container. This method should return a new
#               iterator object that can iterate over all the objects in the container.
#   __next__    For use on iterator objects; return the next item from the container.
#   __call__    Called when the instance is “called” as a function; x(arg1, arg2, ...) is shorthand for
#               x.__call__(arg1, arg2, ...).
#   __len__     Called to implement the built-in function len().

# NESTED CLASS NOTE: Most python developers do NOT use nested/inner classes; nested classes don't reduce/increase
# efficiency but it may alter maintenance and understanding efficiency.


# How to make a basic class
class ExampleObject:
    def __init__(self, name):
        self.name = name
        self.__superprivate = "Super Private Y'all, I won't be overridden by superclasses."
        self._semiprivate = "Semi Private is a little shy..."

    def print_name(self):
        print(self.name)


# How to instantiate a class:
obj_var = ExampleObject("Example One")

# NOTE: print(obj_var.__superprivate) will raise an AttributeError, but the following will work:
print(obj_var._semiprivate)
# BUT you can see __superprivate if you do this:
print(obj_var.__dict__)


class Shape:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides


# This example inherits from Shape and uses decorators for getters, setters, and deleters.
class Square(Shape):
    def __init__(self, height="0", width="0"):
        Shape.__init__(self, 2)
        self.height = height
        self.width = width

    # "Getter"
    @property
    def height(self):
        return self.__height

    # Setter
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Invalid height")

    # Deleter
    @height.deleter
    def height(self):
        del self.__height


    # "Getter"
    @property
    def width(self):
        return self.__width

    # Setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Invalid width")

    # Deleter
    @width.deleter
    def width(self):
        del self.__width

    def get_area(self):
        return int(self.__width) * int(self.__height)

    # How to define a cast of this object to a string type:
    def __str__(self):
        return "This is a {} with {} height and {} width.".format(type(self).__name__, self.__height, self.__width)

    # "Magic" method to compare Square objects:
    def __gt__(self, square2):
        if self.get_area() > square2.get_area():
            return True
        else:
            return False


# Instantiate the Square class:
square = Square()
# Use the Setters
square.height = "10"
square.width = "10"
# Use the Getters
print(square.height)
print(square.width)
print("Area", square.get_area())
print(square)
# Use the Deleter
del square.width


# This example uses the property() function for getters, setters, and deleters.
class Alphabet:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, )


alpha = Alphabet('This is a string in the Alphabet Class...')
print(alpha.value)
alpha.value = 'GfG'
del alpha.value


# This is an example of MULTIPLE INHERITANCE.
class Base1(object):
    def __init__(self):
        self.str1 = "Base Object ONE String"


class Base2:
    def __init__(self):
        self.str2 = "Base Object TWO String"


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

    def print_strs(self):
        print(self.str1, self.str2)


derived = Derived()
derived.print_strs()


# NOTE: Sometimes it is useful to have a data type similar C “struct”, bundling together a few named data items; an
# empty class definition is a good solution:
class Employee:
    pass


john = Employee()  # Create an empty employee record
john.name = 'John Doe'  # Fill the fields of the record
john.dept = 'computer lab'
john.salary = 1000


#################################
# REGEX aka REGULAR EXPRESSIONS #
#################################

# Metacharacters:
#   ^   Matches the beginning
#   $   Matches the end
#   .   Matches any character except newline
#   ?   Matches zero or one occurrence.
#   |   Means OR (Matches with any of the characters separated by it.
#   *   Any number of occurrences (including 0 occurrences)
#   +   One ore more occurrences
#   {}  Indicate number of occurrences of a preceding RE to match.
#   []  Represent a character class
#   ()  Enclose a group of REs
#   \   Used to drop the special meaning of character following it (discussed below)
#   \d  Matches any decimal digit, this is equivalent to the set class [0-9].
#   \D  Matches any non-digit character.
#   \s  Matches any whitespace character.
#   \S  Matches any non-whitespace character
#   \w  Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
#   \W  Matches any non-alphanumeric character.

# NOTE: re.match() checks for a match ONLY at the beginning of a string, re.search() matches ANYWHERE in the string.
# NOTE: Use tools like https://regexr.com/ or https://regex101.com/ to easily create regex

# Need to import re
import re

# Pattern to parse expressions with brackets:
pattern = r'((?P<brackets>[()])|(?P<number>\-?\d*\.?\d+)|(?P<operator>[+\-\*\/]))'

# Pattern to parse expressions with only operators and digits:
pattern = r'((?P<operator>[+\-\*\/]?)(?P<number>\-?\d*\.?\d+))'

# Pattern to validate an expression is only operators and digits:
validate = r'^(-?\d*\.?\d+)((\+|\-|\*|\/)(-?\d*\.?\d+))*$'

input = "2*3+5/6*3+15"

# COMPILE
# For more control of the regular expression, and some performance benefits, compile the pattern before match/search:
prog = re.compile(pattern)
result = prog.match(input)
# The two lines above is equivalent to:
result = re.match(pattern, input)

# COMMON REGEX METHODS:
# The following methods can be used with compiled or non-compiled patterns as demonstrated above.  The methods below are
# are being used in a non-compiled manner, where p is a pattern and s is a string.
#   match(p, s)     Returns only ONE Match object, None if no match, matches at the BEGINNING of string.
#   search(p, s)    Returns only ONE Match object, None if no match, matches ANYWHERE in the string.
#   findall(p, s)   Returns a List of all matches from the string (if None, the list will be empty).
#   finditer(p, s)  Returns a Match Iterator, Iterator MAY NOT have next if no match.
#   split(p, s)     Returns a List of string split wherever a match occurred (if no matches, the list will be empty).
#   sub(p, r, s)    Returns s with all matched p replaced with r, r can be a string or a function, if no match return s.
#   subn(p, r, s)   Same as sub() but returns a tuple (new_s, #_of_subs_made), if no matches returns (s, 0)
#   fullmatch(p, s) Returns only ONE Match object, None if no match, if ALL of the string matches the pattern.
#   escape(s)       Return string with all non-alphanumerics escaped with a backslash. This is useful if you want to
#                   match an arbitrary literal string that may have regular expression metacharacters in it.

# NOTE: Match Objects have boolean value of True; use an if to test for match (a failure will return None).
# How to check (with search) the input string against a regular expression (say to validate it):
if re.search(r'^(-?\d*\.?\d+)((\+|\-|\*|\/)(-?\d*\.?\d+))*$', input):
    print("Input string passes validation!")

# FINDALL
print(re.findall('\d+', "I went to him at 11 A.M. on 4th July 1886"))

# SPLIT
print(re.split('[aeiou]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))

# SUB
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))

# ESCAPE
print(re.escape(validate))

# FINDITER: Get a list of Dictionaries where the key is named subgroup of the pattern and the value is the match.
dl = [m.groupdict() for m in re.finditer(pattern, input)]


the_str = "The ape at the apex"
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])


#########
# STACK #
#########

# Python doesn't have stacks, but it's easy to make one with the following class...

# A simple class stack that only allows pop and push operations
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peek(self, item):
        return self.stack[-1]

    def search(self, item):
        return self.stack.index(item)

    def size(self):
        return len(self.stack)


#########
# QUEUE #
#########

# There are two options, you can (1) make your own queue class or (2) you can import the queue module.

# Option (1) Make your own queue class:
class Queue:

    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    def get(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


# Option (2) Import the Queue Module:
# The queue module implements multi-producer, multi-consumer queues.
# It is especially useful in threaded programming when information must be exchanged safely between multiple threads.
import queue

# Create a queue (with option argument maxsize).
my_queue = queue.Queue(maxsize=20)

# PUT items in the queue.
my_queue.put(1)

# GET (remove and return) an item from the queue,
# BLOCKING if item unavailable, THEN LOCKS queue
print("my_queue.get() gets an item, blocks if unavailable, then locks queue :", my_queue.get())
# UNLOCKS queue
print("my_queue.task_done() releases lock from get()"); my_queue.task_done()
# BLOCKS/waits until queue is EMPTY
print("my_queue.join() waits (BLOCKS) until queue is EMPTY"); my_queue.join()
# Is the queue empty
print("Determine if the queue is empty with my_queue.empty():", my_queue.empty())
# Is the queue full
print("Determine if the queue is full with my_queue.full():", my_queue.full())


#################
# MIN/MAX HEAPS #
#################

# Need to import heapq:
import heapq

# MIN HEAPS (heapq default)

min_heap = [5, 4, 3, 2, 1]
n = 3

# How to CREATE min heap from existing list:
heapq.heapify(min_heap)

# How to PUSH to min heap:
heapq.heappush(min_heap, 0)

# How to POP from min heap:
heapq.heappop(min_heap)

# How to PUSH & POP in one op:
heapq.heappushpop(min_heap, 8)  # Will return smallest item INCLUDING item pushed (8).
heapq.heapreplace(min_heap, 9)  # Will return smallest item NOT INCLUDING item pushed (9).


# How to return a LIST of the N largest items (largest at index 0) in heap:
heapq.nlargest(n, min_heap)

# How to return a LIST of the N smallest items (smallest at index 0) in heap:
heapq.nsmallest(n, min_heap)

# For PEEK & LEN use list operators:
print(min_heap[0])
print(len(min_heap))


# MAX HEAPS
# NOTE: To use max heaps with heapq, you either need to use the underscore methods OR you can negate the values before
# pushing and after popping...

# NOTE: If you start with an empty list, and always use heap push/pop ops, then you don't need to use heapify.

max_heap = [0, 1, 2, 3, 4]

# How to CREATE max heap from existing list:
heapq._heapify_max(max_heap)

# How to PUSH to max heap:
max_heap.append(5)
heapq._siftdown_max(max_heap, 0, len(max_heap)-1)

# How to POP from max heap:
heapq._heappop_max(max_heap)

# How to PUSH & POP in one op:
heapq._heapreplace_max(max_heap, 10)  # Will return largest item NOT INCLUDING item pushed (10).

# How to return a LIST of the N largest items (largest at index 0) in heap:
heapq.nlargest(n, max_heap)

# How to return a LIST of the N smallest items (smallest at index 0) in heap:
heapq.nsmallest(n, max_heap)

# For PEEK & LEN use list operators:
print(max_heap[0])
print(len(max_heap))


############
# CLOSURES #
############

# A closure occurs when a function has access to a local var from an enclosing scope that has finished its execution.

# A simple closure example:
def outer_function():
    message = 'hi'

    def inner_function():
        print(message)
    return inner_function()


outer_function()


# Closures can return a function:
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function   # How to return a function.


function = outer_function('hi')
function()
# The next line is the same as the above two lines.
outer_function('hi')()


# Closure returning a function:
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


outer_function('hi')()


##############
# DECORATORS #
##############

# NOTE: Know and understand Closures before trying to understand Decorators!

# DECORATORS are functions which modify the functionality of other functions.

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()


# SIMPLE PYTHON DECORATOR EXAMPLE USING @ SYNTAX
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function  # This line is the same as: display = decorator_function(display)
def display():
    print('display function ran')


display()


# PYTHON DECORATOR W ARGS EXAMPLE USING @ SYNTAX
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function  # This line is the same as: display = decorator_function(display)
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('john', 35)
display()


# PYTHON CLASS DECORATOR EXAMPLE USING @ SYNTAX
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass  # This line is the same as: display = DecoratorClass(display)
def display():
    print('display function ran')


@DecoratorClass
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('john', 35)
display()


# TIMER CLASS DECORATOR EXAMPLE
class Timer:
    def __init__(self, fn, *params):
        self.function = fn
        self.params = params

    def __call__(self, *args, **kwargs):
        import time
        start_time = time.time()
        result = self.function(*args, **kwargs)
        end_time = time.time()
        print("Execution of {} took {} seconds".format(self.function.__name__, end_time - start_time))
        return result


@Timer
def sleepy_function():
    import time
    time.sleep(random.random())


sleepy_function()


# TYPE CHECKER FUNCTION DECORATOR EXAMPLE:
def type_check(T):
    def decorator(f):
        import functools
        @functools.wraps(f)
        def wrapped(*args):
            if any([not isinstance(i, T) for i in args]):
                raise TypeError(f"Parameters not all of type {T.__name__}!")
            else:
                return f(*args)
        return wrapped
    return decorator


@type_check(int)
def add_ints(*ints):
    return sum(ints)


print(add_ints(1, 2, 3))
try:
    print(add_ints(1, '2', 3))
except:
    pass


# PYTHON LOGGER & TIMER DECORATOR EXAMPLE
from functools import wraps
# The @wraps is used to maintain a decorated functions info.

log_files_to_delete = []


# LOGGER DECORATOR
# After a function is decorated with this, when the function is called, it will write what it was called with to a log.
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    # To clean up later:
    global log_files_to_delete
    log_files_to_delete.append('{}.log'.format(orig_func.__name__))

    # NOTE: Without the use of the wraps decorator factory, the name of orig_func would have been 'wrapper',
    # and the docstring of the original orig_func() would have been lost.
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('{} ran with args: {}, and kwargs: {}'.format(orig_func.__name__, args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


# TIMER DECORATOR
# After a function is decorated with this, when the function is called, the time the function took will be printed.
def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


# NOTE: The following decorated function is eq to my_logger(my_timer(decorated_function(name, age)))
@my_logger  # Executes SECOND
@my_timer   # Executes FIRST
def decorated_function(name, age):
    """Dockstring!"""
    import time
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


# DECORATOR THAT ADDS A METHOD TO A CLASS
def decorate_with_method(name):
    def wrapper(klass):
        setattr(klass, name, eval(name))
        return klass
    return wrapper


# METHOD TO ADD
def method_to_add(self):
    print("Instance class: ", self)


# UNDECORATED CLASS
class PlainKlass:
    pass


# DECORATED CLASS
@decorate_with_method("method_to_add")
class Klass:
    pass


plain = PlainKlass()
decorated_klass = Klass()


def get_class_methods(class_name):
    return [func for func in dir(class_name) if callable(getattr(class_name, func)) and not func.startswith("__")]


print("get_class_methods(plain):", get_class_methods(plain))
print("get_class_methods(decorated_klass):", get_class_methods(decorated_klass))

import os
for s in log_files_to_delete:
    print("os.remove({})".format(s))
    os.remove(s)


#############
# THREADING #
#############

# Due to how Python is implemented, you cannot run two threads in one process at the same time.
# This is because Python creates a single resource per process, the Global Interpreter Lock (GIL),
# which a thread must acquire to run.
#
# Other implementations (like Jython and IronPython, but not PyPy) don't have a GIL, and handle dynamic memory
# management differently, and so can safely run the Python code in multiple threads at the same time.
#
# Several important threading objects are:
#   Lock/RLock  Definition and Examples below.
#   Semaphore   Definition and Examples below.
#   Condition   Definition and Examples below.
#   Event       Thread communication mechanism; uses set(), clear(), and wait() .
#   Barrier     Synchronization primitive for use by a fixed number of threads that need to wait on each other.
#   Timer       Subclass of thread that starts after a specified amount of time.
#
# NOTE: Because of the GIL don't kill python threads, the dead thread won't return the GIL...

from threading import Thread
import time


# Thread example
# NOTE: Threads do not return (Future objects) results.
Thread(target=print, args=("I'm a thread!",)).start()

# Use MAP and LAMBDA to make an anonymous thread execute multiple statements.
Thread(target=map, args=(lambda x: x, (print("hello"), print("world"))))


# Method a thread can call
def nap_time():
    time.sleep(.5)
    return "zzz"


# Create a thread instance, name it, start it, check if it's alive, then join it.
thread = Thread(target=nap_time)
thread.setName("Threaddie Mercury")
thread.start()
print("thread.is_alive():", thread.is_alive())
thread.join(1)              # BLOCKING, so use timeout.


# ThreadPoolExecutor creates a pool of threads, which will be reused.
# NOTE: ThreadPoolExecutors CAN return (Future objects) results.
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=2)
executor.submit(nap_time)                       # NON-BLOCKING
returned_future = executor.submit(nap_time)
executor.shutdown(wait=True)                    # BLOCKING by default, use wait=False to shut down immediately.

# ThreadPoolExecutor using a context manager (to manage creation and destruction)
with ThreadPoolExecutor(max_workers=2) as executor_context_manager:
    returned_future = executor_context_manager.submit(nap_time)
    executor_context_manager.submit(print, "I'm a ThreadPoolExecutor Thread!")

# How to get the number and list of active threads:
import threading
print("Active Thread:", threading.activeCount())
print("Thread Objects:", threading.enumerate())


##########
# FUTURE #
##########

# The Future class encapsulates the asynchronous execution of a callable.
# Future instances are created by Executor.submit().
#
# Future methods include:
#   cancel()                Attempt to cancel the call; return False if done/executing, else cancel and return True.
#   cancelled()             Return True if the call was cancelled.
#   running()               Return True if the call is currently being executed and cannot be cancelled.
#   done()                  Return True if the call was successfully cancelled or finished.
#   result(timeout=None)    BLOCKING, Return the value returned by the call, timeout (seconds) can be int or float.
#   add_done_callback(fn)   Attaches the callable fn to the future. fn will be called with the future as its only
#                           argument, when the future is cancelled or finishes running.
#
# NOTE: Helpful Future Module Functions include WAIT and AS_COMPLETED, see docs for more info.

print("returned_future.done():", returned_future.done())
print("returned_future.result(timeout=10):", returned_future.result(timeout=10))


########
# LOCK #
########

# A PRIMITIVE lock is a synchronization primitive, has two states; "locked" or "unlocked"
# Primitive lock methods include:
#   locked()                            Returns True if the lock is acquired.
#   release()                           Release a lock, can be called from ANY thread, not just thread holding lock.
#   acquire(blocking=True, timeout=-1)  Acquire a lock, BLOCKING or NON-BLOCKING, timeout is in seconds, returns True
#                                       if able to acquire lock else returns False.
# NOTE: Can only acquire (lock) primitive locks ONCE.

primitive_lock = threading.Lock()
print("Acquire a lock via primitive_lock.acquire():", primitive_lock.acquire())  # BLOCKING if locked.
print("Try to acquire again, primitive_lock.acquire(timeout=1):", primitive_lock.acquire(timeout=.5))
# Example of a DIFFERENT thread unlocking the lock.
Thread(target=primitive_lock.release).start()
print("primitive_lock.locked():", primitive_lock.locked())

# A REENTRANT lock is a synchronization primitive that may be acquired multiple times by the same thread. Internally,
# it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked state used by
# primitive locks. In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.
# Reentrant lock uses acquire and release (no locked).

reentrant_lock = threading.RLock()
reentrant_lock.acquire()  # BLOCKING if locked.
# OWNING thread must unlock, else "RuntimeError: cannot release un-acquired lock"
Thread(target=reentrant_lock.release).start()


#############
# SEMAPHORE #
#############

# A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release()
# call. The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other
# thread calls release().

semaphore = threading.Semaphore(value=1)
Thread(target=semaphore.acquire, kwargs={"timeout": .2}).start()
semaphore.acquire(timeout=.2)


########################
# CONDITION (VARIABLE) #
########################

# A condition represents some kind of state change in the application; a thread can wait for a given condition, or
# signal that the condition has happened.
#
# A condition variable is always associated with some kind of lock; this can be passed in or one will be created by
# default. Passing one in is useful when several condition variables must share the same lock. The lock is part of the
# condition object: you don’t have to track it separately.
#
# Methods for the Condition Object include:
#   acquire(*args)              Acquire the underlying lock, via calling its method, returns that methods return.
#   release()                   Releases the underlying lock, via calling its method, no return value.
#   wait(timeout=None)          Wait until notified or until a timeout occurs. This method releases the underlying lock,
#                               and then blocks until it is awakened by a notify() or notify_all() call for the same
#                               condition variable in another thread, or until the optional timeout occurs. Once
#                               awakened or timed out, it re-acquires the lock and returns.
#   wait_for(p, timeout=None)   Wait until a condition p evaluates to true. p should be a callable which result will be
#                               interpreted as a boolean value. timeout is the maximum time to wait.
#   notify(n=1)                 Wake up n thread(s) waiting on this condition, if any. DOES NOT release the lock.
#   notify_all()                Wake up n thread(s) waiting on this condition, if any. DOES NOT release the lock.

# CONDITION VARIABLE both producers and consumers act on.
condition_variable = threading.Condition()


# Predicate representing the state.
def is_available():
    return True


# This represents consuming something from a shared resource.
def consume_something():
    pass


# This represents producing something to a shared.
def produce_something():
    pass


# NOTE: Using Context Manager will handle acquire() and release() calls.

# CONSUMER USAGE via wait
with condition_variable:
    while not is_available():
        condition_variable.wait()
    consume_something()

# CONSUMER USAGE via wait_for
with condition_variable:
    condition_variable.wait_for(is_available)
    consume_something()

# PRODUCER USAGE
with condition_variable:
    produce_something()
    condition_variable.notify()


###################
# MULTIPROCESSING #
###################

# Processes via the multiprocessing package supports spawning processes using an API similar to the threading module.
# The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global
# Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the
# programmer to fully leverage multiple processors on a given machine.
#
# Depending on the platform, multiprocessing supports three ways to start a process. These start methods are:
#   spawn       Parent process starts a fresh python process, ONLY inherits necessary resources to run run().
#   fork        Parent process uses os.fork() to fork python, child is identical to parent (w/ ALL resources).
#   forkserver  Server process started, from then on parent connects to server and requests that it forks a new process.
#               Fork server process is a single thread (safe to use os.fork()), no unnecessary resources are given.
#
# The Process signature is Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None), note that
# MULTIPROCESSING COMMUNICATION is supported (via Queues and Pipes), process can be SYNCHRONIZED (via Locks and
# Connection Objects), and processes can SHARE STATE (via shared memory, or server process).
# See the python documentation for more info.
from multiprocessing import Process

Process(target=print, args=("I'm a Process!",)).start()


# Method a process can call
def nap_time():
    time.sleep(1)
    return "zzz"


process = Process(target=nap_time, name="Process-or Snape")
process.start()
print("process.name", process.name)
print("process.pid:", process.pid)
print("process.is_alive():", process.is_alive())
process.join(10)
print("process.exitcode:", process.exitcode)

# ProcessPoolExecutor creates a pool of process, which will be reused.
# NOTE: ProcessPoolExecutor CAN return (Future objects) results.
from concurrent.futures import ProcessPoolExecutor

executor = ProcessPoolExecutor(max_workers=2)
executor.submit(nap_time)                       # NON-BLOCKING
executor.shutdown(wait=True)                    # BLOCKING by default, use wait=False to shut down immediately.

future_obj = None

# ThreadPoolExecutor using a context manager (to manage creation and destruction)
with ProcessPoolExecutor(max_workers=2) as executor_context_manager:
    future_obj = executor_context_manager.submit(nap_time)
    executor_context_manager.submit(print, "I'm a ProcessPoolExecutor Thread!")

if future_obj.done():
    print("future_obj.result(timeout=1):", future_obj.result(timeout=1))





