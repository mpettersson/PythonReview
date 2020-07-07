"""
    URLIFY (CCI 1.3)

    Write a method to replace all spaces in a string with '%20'.  You may assume that the string has sufficient space at
    the end to hold the additional characters, and that you are given the "true" length of the string.

    NOTE: If implementing in Java, please use a character array so that you can perform this operation in place.

    Example:
        Input = "Mr John Smith    ", 13
        Output = "Mr%20John%20Smith"

    NOTE: This question isn't really aimed at Python; normally, you'd work from back to front moving a single char at a
    time, while replacing spaces with '%20'.
"""


def urlify(string : str, l = None):
    return string.strip(" ").replace(" ", "%20")


print(urlify("Mr John Smith    "))

