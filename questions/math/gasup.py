"""
    THE GASUP PROBLEM (EPI 18.6)

    In the gasup problem, a number of cities are arranged on a circular road.  You need to visit all the cities and
    come back to the starting city.  A certain amount of gas is available at each city.  The amount of gas summed up
    over all cities is equal to the amount of gas required to go around the road once.  Your gas tank has unlimited
    capacity.  Call a city ample if you can begin at that city with an empty tank, refill at it, then travel through all
    the remaining cities, refilling at each, and return to the ample city, without running out of gas at any point.

    Given an instance of the gasup problem, how would you efficiently compute an ample city?  You can assume that there
    exists an ample city.

    Example:
        Input = [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]
        Output =

    Variations:
        - Solve the same problem when you cannot assume that there exists an ample city.
        - SEE: https://leetcode.com/problems/gas-station/
"""


# Naive/Brute Force Approach:  Time complexity is O(n**2), where n is the number of cities.  Space complexity is O(n),
# where n is the number of cities.
#
# NOTE: This provides a list of ALL ample cities, empty list if none.
def find_ample_cities_naive(gallons, distance):
    if gallons is not None and distance is not None and len(gallons) is len(distance):
        result = []
        mpg = 20
        n = len(gallons)
        for orig in range(n):
            gas = 0
            ran_out_flag = False
            for i in range(n):
                offset = (orig + i) % n
                gas += gallons[offset] - distance[offset] / mpg
                if gas < 0:
                    ran_out_flag = True
            if not ran_out_flag:
                result.append(orig)
        return result


# Optimal Approach:  Time complexity is O(n), where n is the number of cities.  Space complexity is O(1).
#
# NOTE: This returns only ONE ample city; the FIRST one that it encounters.
def find_ample_city(gallons, distance):
    city = gas = negative_gas = 0
    mpg = 20
    for i in range(len(gallons)):
        gas += gallons[i] - distance[i] / mpg           # Update gas level.
        if gas < 0:                                     # If we didn't make it to the current city:
            negative_gas += gas                         # Track total negative gas amount for return conditional.
            gas = 0                                     # Start tracking with empty tank...
            city = i + 1                                # Update to next possible city.
    return city if negative_gas + gas >= 0 else None    # Check if there was mathematically enough gas.


gallon_distance_tuples = [([50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]),
                          ([1, 2, 3, 4, 5], [60, 80, 100, 20, 40]),
                          ([2, 3, 4], [60, 80, 60]),
                          ([5, 10, 10, 10, 10, 10, 15], [200, 200, 200, 200, 200, 200, 200]),
                          ([15, 5, 10, 15, 5, 10, 10], [200, 200, 200, 200, 200, 200, 200])]

for gallons, distance in gallon_distance_tuples:
    print(f"gallons: {gallons}\ndistance: {distance}")
    print(f"find_ample_cities_naive(gallons, distance): {find_ample_cities_naive(gallons, distance)}")
    print(f"find_ample_city(gallons, distance): {find_ample_city(gallons, distance)}")
    print()


