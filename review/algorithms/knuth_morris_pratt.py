"""
    KNUTH MORRIS PRATT

    Average Runtime:    O(n + m)
    Worst Runtime:      O(n * m)    (when each window has a spurious, or false, match)
    Best Runtime:       O(n + m)
    Space Complexity:   O(1)
    Alg Paradigm:       String Search

    The Knuth Morris Pratt (KMP) string search algorithm searches for occurrences of a word string W within a main text
    string S by employing the observation that when a mismatch occurs, the word itself contains sufficient information
    to determine where the next match could begin, thus bypassing re-examination of previously matched characters.

    SEE:  wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
"""




