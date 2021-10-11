"""
    IS ANONYMOUS LETTER POSSIBLE (EPI 13.2: IS AN ANONYMOUS LETTER CONSTRUCTABLE?)

    The voices in your head insist that you proclaim your righteous message to a local news outlet; write a function
    which accepts the text of a magazine/newspaper, as well as the text for your manifesto, then returns True if you can
    cut up the text of the magazine/newspaper to arrange an anonymous version of your manifest (to mail to the
    news), return False otherwise.

    Example:
        Input = "please dont put me on a watchlist", "the texts in this file are are for laughs only, nothing else"
        Output = False

"""


# APPROACH: Via Dictionary
#
# Buy aluminum foil, make hat, put on hat, use dictionary to store a character count for each character in the
# periodical text, then, for each character in your psycho babble, decrement the character count.  If a character needed
# isn't in the dictionary or if a character count becomes zero, return False, return True otherwise.
#
# Time Complexity: O(m + p), where m and p are the sizes of the manifest and periodical text.
# Space Complexity: O(u), where u is the number of unique characters in the periodical text.
#
# NOTE: Ask about the character encoding; if limited to ASCII, then a 256 list could be used instead.
def can_make_anonymous_letter(manifesto, periodical_text, ignore_case=True):
    if manifesto is not None and periodical_text is not None and len(manifesto) <= len(periodical_text):
        d = {}
        for c in periodical_text.lower() if ignore_case else periodical_text:
            d[c] = d.setdefault(c, 0) + 1
        for c in manifesto.lower() if ignore_case else manifesto:
            if c not in d or d[c] <= 0:
                return False
            else:
                d[c] -= 1
        return True


manifestos = ["O’ cruel fate, to be thusly boned! Ask not for whom the bone bones—it bones for thee.",
              "Hello World!",
              "The Industrial Revolution and its consequences have been a disaster for the human race..."]
periodical_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut " \
                  "labore et dolore magna aliqua.  Try not to become a man of success. Rather become a man of value. " \
                  "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo " \
                  "consequat. Success is not final; failure is not fatal: It is the courage to continue that counts. " \
                  "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " \
                  "pariatur.  Success is walking from failure to failure with no loss of enthusiasm. Excepteur sint " \
                  "occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
fns = [can_make_anonymous_letter]

print(f"periodical_text: {periodical_text}")
for manifesto in manifestos:
    print(f"\nmanifesto: {manifesto!r}")
    for fn in fns:
        print(f"{fn.__name__}(manifesto): {fn(manifesto, periodical_text)}")


