"""
    EXCHANGE RATE MANIPULATION

    Given a set of exchange rates (below), write a program that determines if an arbitrage exists, i.e., there is a way
    by which you can start with one unit of some currency C and perform a series of barters which results in having more
    than one unit of C.

             USD      EUR     GBP     JPY     CHF     CAD     AUD
    USD       1     0.8123  0.6404  78.125  0.9784  0.9924  0.9465
    EUR     1.2275    1     0.7860  96.55   1.2010  1.2182  1.1616
    GBP     1.5617  1.2724    1     122.83  1.5280  1.5498  1.4778
    JPY     0.0128  0.0104  0.0081    1     1.2442  0.0126  0.0120
    CHF     1.0219  0.8327  0.6546  80.39     1     1.0142  0.9672
    CAD     1.0076  0.8206  0.6453  79.26   0.9859    1     0.9535
    AUD     1.0567  0.8609  0.6767  83.12   1.0339  1.0487    1

    Example:
        1 USD --> CHF --> JPY --> 1.00385609212 USD

    Note: This resembles a weighted graph problem...

    This question is from Elements of Programming Interviews; SEE https://elementsofprogramminginterviews.com/.
"""








