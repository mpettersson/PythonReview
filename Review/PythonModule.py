# A SINGLE LEADING UNDERSCORE is a weak "internal use" indicator.
# For example "from MyModule import *" does not import objects whose name starts with an underscore.
_single_leading_underscore_variable = "weak internal use"


def _single_leading_underscore_function():
    print("I'm inside _single_leading_underscore_function().")
    print("I won't be imported if you 'from MyModule import *'.")


# DOUBLE LEADING UNDERSCORES is NAME MANGLING and can have at most one trailing underscore.
# Name Mangling is used to ensure that subclasses don't accidentally override the private methods and attributes of
# their superclasses.
# It's not designed to prevent deliberate access from outside.
# Using Double Leading Underscores in Modules isn't usual.
__double_leading_underscore_variable = "Name Mangling"


def __double_leading_underscore_function():
    print("I'm inside __double_leading_underscore_function().")


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


def print_hello_world():
    print("Hello World")


def print_foo_bar():
    print("foo bar")


# NOTE: To run a Python module from the CLI with arguments (i.e., python3 PythonModule.py <arguments>)
# the if __name__ == "__main__": part ought to be included at the bottom of the file:
if __name__ == "__main__":
    factorial(10)

    # NOTE: the following is how you'd use arguments supplied to the module from the CLI (sys.argv[0] is script name):
    # import sys
    # factorial(int(sys.argv[1]))


