"""
    THE KNAPSACK PROBLEMS

    From Wikipedia (SEE: wikipedia.org/wiki/Knapsack_problem):

        The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a
        weight and a value, determine the number of each item to include in a collection so that the total
        weight is less than or equal to a given limit and the total value is as large as possible. It derives
        its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill
        it with the most valuable items. The problem often arises in resource allocation where the decision
        makers have to choose from a set of non-divisible projects or tasks under a fixed budget or time
        constraint, respectively.

        The knapsack problem has been studied for more than a century, with early works dating as far back as
        1897. The name "knapsack problem" dates back to the early works of the mathematician Tobias Dantzig
        (1884–1956), and refers to the commonplace problem of packing the most valuable or useful items
        without overloading the luggage.

    The most common Knapsack problems include:
        The 01 Knapsack Problem
            - Given a set of items that each have a value and a weight, determine which of those items to select to as
              to maximize the total value, constrained by the given knapsack's capacity.
            - SEE: knapsack_01.py
        The Bounded Knapsack Problem (BKP)
            - Given a set of items that each have a value, a weight, and a number of units, determine the number of
              items and units to select as to maximize the total value, constrained by the given knapsack's capacity.
            - SEE: knapsack_bounded.py
        The Unbounded Knapsack Problem (UKP)
            - Given a set of items that each have a value, a weight, and an unlimited (unbounded) number of units,
              determine the set of items to select as to maximize the total value, constrained by the given knapsack's
              capacity.
            - SEE: knapsack_unbounded.py

    TODO: This section needs to be finished...
    Other variations include:
        Fractional, or continuous, Knapsack problems.
        Knapsack problems with real number weights.
        Multi-objective knapsack problem
            This variation changes the goal of the individual filling the knapsack. Instead of one objective, such as
            maximizing the monetary profit, the objective could have several dimensions. For example, there could be
            environmental or social concerns as well as economic goals. Problems frequently addressed include portfolio
            and transportation logistics optimizations.[21][22]
            As an example, suppose you ran a cruise ship. You have to decide how many famous comedians to hire. This
            boat can handle no more than one ton of passengers and the entertainers must weigh less than 1000 lbs. Each
            comedian has a weight, brings in business based on their popularity and asks for a specific salary. In this
            example, you have multiple objectives. You want, of course, to maximize the popularity of your entertainers
            while minimizing their salaries. Also, you want to have as many entertainers as possible.
        Multi-dimensional knapsack problem
            In this variation, the weight of knapsack item i is given by a D-dimensional vector and the knapsack has a
            D-dimensional capacity vector. The target is to maximize the sum of the values of the items in the knapsack
            so that the sum of weights in each dimension does not exceed.
        Multiple knapsack problem
            This variation is similar to the Bin Packing Problem. It differs from the Bin Packing Problem in that a
            subset of items can be selected, whereas, in the Bin Packing Problem, all items have to be packed to certain
            bins. The concept is that there are multiple knapsacks. This may seem like a trivial change, but it is not
            equivalent to adding to the capacity of the initial knapsack. This variation is used in many loading and
            scheduling problems in Operations Research and has a Polynomial-time approximation scheme.
        Quadratic knapsack problem
            The quadratic knapsack problem maximizes a quadratic objective function subject to binary and linear
            capacity constraints. The problem was introduced by Gallo, Hammer, and Simeone in 1980, however the first
            treatment of the problem dates back to Witzgall in 1975.
        Subset-sum problem
            The subset sum problem is a special case of the decision and 0-1 problems where each kind of item, the
            weight equals the value. In the field of cryptography, the term knapsack problem is often used to refer
            specifically to the subset sum problem and is commonly known as one of Karp's 21 NP-complete problems.
            The generalization of subset sum problem is called multiple subset-sum problem, in which multiple bins exist
            with the same capacity. It has been shown that the generalization does not have an FPTAS.
        Geometric knapsack problem
            In the geometric knapsack problem, there is a set of rectangles with different values, and a rectangular
            knapsack. The goal is to pack the largest possible value into the knapsack.


    TODO: Compile all of the used 'items' lists here for reference.
    Example:
        Input = [(65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (99, 10), (275, 85), (155, 25), (120, 30), (75, 75),
                 (320, 65), (40, 10), (200, 95), (100, 50), (220, 40), (150, 70)], 130  # (price, weight), total_weight
        Output = 695    # Max value set: [(155, 25), (320, 65), (220, 40)]

    Example Variations:
        - Solve the same problem using O(w) space, where w is the initial capacity.
        - Solve the same problem using O(c) space, where c is the number of weights between 0 and w that can be
          achieved. For example, if the weights are 100, 200, 200, 500, and w=853, then c=9, corresponding to the
          weights 0, 100, 200, 300, 400, 500, 600, 700, 800.
        - Solve the fractional knapsack problem. In this formulation, the thief can take a fractional part of an item,
          e.g., by breaking it.  Assume the value of a fraction of an item is that fraction times the value of the item.
        - In the 'divide-the-spoils-fairly' problem, two thieves who have successfully completed a burglary want to know
          how to divide the stolen items into two groups such that the difference between the value of these two groups
          is minimized. Write a program to solve the divide-the-spoils-fairly problem.
        - Solve the divide-the-spoils-fairly problem with the additional constraint that the thieves have the same
          number of items.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible values for capacity (int, None, negative, etc.)?
#   - Does the full capacity need to be used (what should happen if can't use total capacity)?
#   - What should be returned (total, or list of items, what should happen if failure)?
#   - What are the possible sizes of the list (empty, max size)?
#   - What are the possible values in the list (int/float/None/negative)?
#   - Can the list have unique/duplicate values?
#   - Will the list be sorted?
#   - Can the list be modified?


