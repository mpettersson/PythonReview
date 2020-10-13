"""
    SCHEDULE TO MINIMIZE WAITING TIME (EPI 18.2)

    A database has to respond to a set of client SQL queries.  The service time required for each query is known in
    advance.  For this application, the queries must be processed by the database one at a time, but can be done in any
    order.  The time a query waits before its turn comes is called its waiting time.

    Given service times for a set of queries, compute a schedule for processing the queries that minimizes the total
    waiting time.  Return the minimum waiting time.

    Consider the following schedule times for [2, 5, 1, 3]:
             Order                  Times              Total
            -------     ---------------------------    -----
            2,5,1,3     (0) + (2) + (2+5) + (2+5+1)     17
            5,3,2,1     (0) + (5) + (5+3) + (5+3+2)     23

    Example:
        Input = [2, 5, 1, 3]
        Output = 10
"""


# Greedy Approach:  Time complexity is O(n * log(n)), where n is the number of elements in the list.  Space complexity
# is O(1).
def schedule_min_waiting_time(l):
    if l is not None:
        l.sort()
        total_waiting_time = 0
        elapsed_time = 0
        for i in range(len(l)):
            total_waiting_time += elapsed_time
            elapsed_time += l[i]
        return total_waiting_time


times_list = [[2, 5, 1, 3],
              [5, 3, 2, 1],
              [8, 3, 8, 0, 8, 5, 7, 7, 6, 1],
              [],
              None]

for t in times_list:
    print(f"schedule_min_waiting_time({t}): {schedule_min_waiting_time(t)}")


