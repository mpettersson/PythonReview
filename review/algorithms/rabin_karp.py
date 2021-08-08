"""
    RABIN KARP

    Average Runtime:    O(n + m)
    Worst Runtime:      O(n * m)    (when each window has a spurious, or false, match)
    Best Runtime:       O(n + m)
    Space Complexity:   O(1)
    Alg Paradigm:       String Search

    The Rabin–Karp algorithm or Karp–Rabin algorithm is a string searching algorithm created by Richard M. Karp and
    Michael O. Rabin (1987) that uses hashing to find an exact match of a pattern string in a text. It uses a rolling
    hash (window) to quickly filter out positions of the text that cannot match the pattern, and then checks for a match
    at the remaining positions. Generalizations of the same idea can be used to find more than one match of a single
    pattern, or to find matches for more than one pattern.

    SEE: wikipedia.org/wiki/Rabin–Karp_algorithm
"""

# d is the number of characters in the input alphabet
d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number


def search(pat, txt, q):
    len_pat = len(pat)
    len_txt = len(txt)
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)% q"
    for i in range(len_pat - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(len_pat):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(len_txt - len_pat + 1):
        # Check the hash values of current window of text and pattern if the hash values match then only check for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(len_pat):
                if txt[i + j] != pat[j]:
                    break
            j += 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == len_pat:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < len_txt - len_pat:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + len_pat])) % q

            if t < 0:
                t = t + q           # t rolled over/went negative; make it pos by adding q.


txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101  # A prime number
search(pat, txt, q)

