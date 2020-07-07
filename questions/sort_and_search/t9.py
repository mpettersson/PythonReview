"""
    T9

    On old cell phones, users typed on a numberic keypad and the phone would provide a list of words that matched these
    numbers.  Each digit mapped to a set of 0-4 letters.  Implement an algorithm to return a list of matching words,
    given a sequence of digits.  You are provided a list of valid words (provided in whatever data structure you'd
    like).

    The mapping is:
        0 -> None
        1 -> None
        2 -> abc
        3 -> def
        4 -> ghi
        5 -> jkl
        6 -> mno
        7 -> pqrs
        8 -> tuv
        9 -> wxyz

    Example:
        input = 8733
        output = [tree, used]
"""


def preprocess_word_list(l):
    word_dict = dict()
    if l is None or len(l) is 0:
        return word_dict
    for s in l:
        key = ""
        for c in s:
            if c == "a" or c == "b" or c == "c":
                key = key + "2"
            elif c == "d" or c == "e" or c == "f":
                key = key + "3"
            elif c == "g" or c == "h" or c == "i":
                key = key + "4"
            elif c == "j" or c == "k" or c == "l":
                key = key + "5"
            elif c == "m" or c == "n" or c == "o":
                key = key + "6"
            elif c == "p" or c == "q" or c == "r" or c == "s":
                key = key + "7"
            elif c == "t" or c == "u" or c == "v":
                key = key + "8"
            elif c == "w" or c == "x" or c == "y" or c == "z":
                key = key + "9"
        int_key = int(key)
        if int_key in word_dict.keys():
            word_dict[int_key].append(s)
        else:
            word_dict[int_key] = [s]
    return word_dict


def t9(num, word_dict):
    if num in word_dict.keys():
        return word_dict[num]
    else:
        return []


word_list = ['known', 'aching', 'you', 'goodbye', 'never', 'give', 'up', 'on', "would", "have", 'let', 'too', 'gonna',
             'any', 'guy', 'how', 'each', 'see', 'inside', 'tell', 'full', 'been', 'know', 'cry', 'a', 'ooh', 'are',
             'strangers', 'just', 'around', 'what', 'long', 'thinking', 'play', 'this', 'understand', 'feeling', 'down',
             'make', 'desert', 'say', 'love', 'run', 'no', 'me', 'heart', 'to', 'shy', 'but', 'get', 'it', 'we', 'and',
             'if', 'blind', 'other', 'gotta', 'ask', 'going', 'of', 'both', 'am', 'commitment', 'game', 'i', 'not',
             'for', 'so', 'the', 'wanna', 'from', 'lie', 'do', 'hurt', 'your', 'rules', 'creative', 'reactive', 'race',
             'care', 'acre', 'angered', 'enraged', 'death', 'hated', 'admirer', 'married', 'leaf', 'flea', 'funeral',
             'listens', 'silent', 'elvis', 'lives']

num_none = 80085
num_one = 4
num_two = 2273
print("num_none: ", num_none)
print("num_one: ", num_one)
print("num_two: ", num_two)

preprocessed_dict = preprocess_word_list(word_list)
print("t9(num_none, preprocessed_dict):", t9(num_none, preprocessed_dict))
print("t9(num_one, preprocessed_dict):", t9(num_one, preprocessed_dict))
print("t9(num_two, preprocessed_dict):", t9(num_two, preprocessed_dict))




