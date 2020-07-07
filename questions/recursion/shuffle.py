"""
    SHUFFLE

    Write a method to shuffle a deck of cards.  It must be a perfect shuffle--in other words, each of the 52!
    permutations of the deck has to be equally likely.  Assume that you are given a random number generator which is
    perfect.
"""
import random


def shuffle_recursive(deck, i=None):
    if i is None:
        i = len(deck) - 1
    if i is 0:
        return deck
    shuffle_recursive(deck, i - 1)
    k = random.randint(0, i)
    deck[i], deck[k] = deck[k], deck[i]
    return deck


def shuffle_iteratively(deck):
    for i in range(len(deck)):
        k = random.randint(0, i)
        deck[i], deck[k] = deck[k], deck[i]
    return deck


ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♤", "♧", "♥", "♦"]
deck = [r+s for r in ranks for s in suits]

deck.sort()
print("deck:", deck)
print("shuffle_recursive(deck):", shuffle_recursive(deck))
deck.sort()
print("shuffle_iteratively(deck):", shuffle_iteratively(deck))
