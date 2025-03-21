"""
    BINARY WATCH TIME  (leetcode.com/problems/binary-watch)

    Write a function which takes an integer n that represents the total number of LEDs lit on a binary watch and returns
    all possible times.

    The binary watch has 4 LEDs on the top representing hours (0-11), and the 6 LEDs on the bottom representing minutes
    (0-59), where LED represents a zero or one, with the least significant bit on the right.

    For example, given the binary watch (where ◼ represents an illuminated led and ◻ is not illuminated):
        H: ◻◼◻◻
        M: ◼◼◻◻◼◼
    The time would be 4:51.

    Example:
        Input = 1
        Output = ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
"""
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Input Validation?
#   - What about AM/PM?


# APPROACH: Brute Force/Lookup Table
#
# This is not the solution that the interviewer wants; regardless of being whimsical, and very quick...
#
# Time Complexity: O(1).
# Space Complexity: O(1), there are a finite number of valid time combinations (the most is 190 if 5 LEDs are lit).
def binary_watch_time_via_lookup_table(n):
    if isinstance(n, int) and 0 <= n <= 10:
        d = {0: ['0:00'],
             1: ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00'],
             2: ['0:03', '0:05', '0:06', '0:09', '0:10', '0:12', '0:17', '0:18', '0:20', '0:24', '0:33', '0:34', '0:36', '0:40', '0:48', '1:01', '1:02', '1:04', '1:08', '1:16', '1:32', '2:01', '2:02', '2:04', '2:08', '2:16', '2:32', '3:00', '4:01', '4:02', '4:04', '4:08', '4:16', '4:32', '5:00', '6:00', '8:01', '8:02', '8:04', '8:08', '8:16', '8:32', '9:00', '10:00'],
             3: ['0:07', '0:11', '0:13', '0:14', '0:19', '0:21', '0:22', '0:25', '0:26', '0:28', '0:35', '0:37', '0:38', '0:41', '0:42', '0:44', '0:49', '0:50', '0:52', '0:56', '1:03', '1:05', '1:06', '1:09', '1:10', '1:12', '1:17', '1:18', '1:20', '1:24', '1:33', '1:34', '1:36', '1:40', '1:48', '2:03', '2:05', '2:06', '2:09', '2:10', '2:12', '2:17', '2:18', '2:20', '2:24', '2:33', '2:34', '2:36', '2:40', '2:48', '3:01', '3:02', '3:04', '3:08', '3:16', '3:32', '4:03', '4:05', '4:06', '4:09', '4:10', '4:12', '4:17', '4:18', '4:20', '4:24', '4:33', '4:34', '4:36', '4:40', '4:48', '5:01', '5:02', '5:04', '5:08', '5:16', '5:32', '6:01', '6:02', '6:04', '6:08', '6:16', '6:32', '7:00', '8:03', '8:05', '8:06', '8:09', '8:10', '8:12', '8:17', '8:18', '8:20', '8:24', '8:33', '8:34', '8:36', '8:40', '8:48', '9:01', '9:02', '9:04', '9:08', '9:16', '9:32', '10:01', '10:02', '10:04', '10:08', '10:16', '10:32', '11:00'],
             4: ['0:15', '0:23', '0:27', '0:29', '0:30', '0:39', '0:43', '0:45', '0:46', '0:51', '0:53', '0:54', '0:57', '0:58', '1:07', '1:11', '1:13', '1:14', '1:19', '1:21', '1:22', '1:25', '1:26', '1:28', '1:35', '1:37', '1:38', '1:41', '1:42', '1:44', '1:49', '1:50', '1:52', '1:56', '2:07', '2:11', '2:13', '2:14', '2:19', '2:21', '2:22', '2:25', '2:26', '2:28', '2:35', '2:37', '2:38', '2:41', '2:42', '2:44', '2:49', '2:50', '2:52', '2:56', '3:03', '3:05', '3:06', '3:09', '3:10', '3:12', '3:17', '3:18', '3:20', '3:24', '3:33', '3:34', '3:36', '3:40', '3:48', '4:07', '4:11', '4:13', '4:14', '4:19', '4:21', '4:22', '4:25', '4:26', '4:28', '4:35', '4:37', '4:38', '4:41', '4:42', '4:44', '4:49', '4:50', '4:52', '4:56', '5:03', '5:05', '5:06', '5:09', '5:10', '5:12', '5:17', '5:18', '5:20', '5:24', '5:33', '5:34', '5:36', '5:40', '5:48', '6:03', '6:05', '6:06', '6:09', '6:10', '6:12', '6:17', '6:18', '6:20', '6:24', '6:33', '6:34', '6:36', '6:40', '6:48', '7:01', '7:02', '7:04', '7:08', '7:16', '7:32', '8:07', '8:11', '8:13', '8:14', '8:19', '8:21', '8:22', '8:25', '8:26', '8:28', '8:35', '8:37', '8:38', '8:41', '8:42', '8:44', '8:49', '8:50', '8:52', '8:56', '9:03', '9:05', '9:06', '9:09', '9:10', '9:12', '9:17', '9:18', '9:20', '9:24', '9:33', '9:34', '9:36', '9:40', '9:48', '10:03', '10:05', '10:06', '10:09', '10:10', '10:12', '10:17', '10:18', '10:20', '10:24', '10:33', '10:34', '10:36', '10:40', '10:48', '11:01', '11:02', '11:04', '11:08', '11:16', '11:32'],
             5: ['0:31', '0:47', '0:55', '0:59', '1:15', '1:23', '1:27', '1:29', '1:30', '1:39', '1:43', '1:45', '1:46', '1:51', '1:53', '1:54', '1:57', '1:58', '2:15', '2:23', '2:27', '2:29', '2:30', '2:39', '2:43', '2:45', '2:46', '2:51', '2:53', '2:54', '2:57', '2:58', '3:07', '3:11', '3:13', '3:14', '3:19', '3:21', '3:22', '3:25', '3:26', '3:28', '3:35', '3:37', '3:38', '3:41', '3:42', '3:44', '3:49', '3:50', '3:52', '3:56', '4:15', '4:23', '4:27', '4:29', '4:30', '4:39', '4:43', '4:45', '4:46', '4:51', '4:53', '4:54', '4:57', '4:58', '5:07', '5:11', '5:13', '5:14', '5:19', '5:21', '5:22', '5:25', '5:26', '5:28', '5:35', '5:37', '5:38', '5:41', '5:42', '5:44', '5:49', '5:50', '5:52', '5:56', '6:07', '6:11', '6:13', '6:14', '6:19', '6:21', '6:22', '6:25', '6:26', '6:28', '6:35', '6:37', '6:38', '6:41', '6:42', '6:44', '6:49', '6:50', '6:52', '6:56', '7:03', '7:05', '7:06', '7:09', '7:10', '7:12', '7:17', '7:18', '7:20', '7:24', '7:33', '7:34', '7:36', '7:40', '7:48', '8:15', '8:23', '8:27', '8:29', '8:30', '8:39', '8:43', '8:45', '8:46', '8:51', '8:53', '8:54', '8:57', '8:58', '9:07', '9:11', '9:13', '9:14', '9:19', '9:21', '9:22', '9:25', '9:26', '9:28', '9:35', '9:37', '9:38', '9:41', '9:42', '9:44', '9:49', '9:50', '9:52', '9:56', '10:07', '10:11', '10:13', '10:14', '10:19', '10:21', '10:22', '10:25', '10:26', '10:28', '10:35', '10:37', '10:38', '10:41', '10:42', '10:44', '10:49', '10:50', '10:52', '10:56', '11:03', '11:05', '11:06', '11:09', '11:10', '11:12', '11:17', '11:18', '11:20', '11:24', '11:33', '11:34', '11:36', '11:40', '11:48'],
             6: ['1:31', '1:47', '1:55', '1:59', '2:31', '2:47', '2:55', '2:59', '3:15', '3:23', '3:27', '3:29', '3:30', '3:39', '3:43', '3:45', '3:46', '3:51', '3:53', '3:54', '3:57', '3:58', '4:31', '4:47', '4:55', '4:59', '5:15', '5:23', '5:27', '5:29', '5:30', '5:39', '5:43', '5:45', '5:46', '5:51', '5:53', '5:54', '5:57', '5:58', '6:15', '6:23', '6:27', '6:29', '6:30', '6:39', '6:43', '6:45', '6:46', '6:51', '6:53', '6:54', '6:57', '6:58', '7:07', '7:11', '7:13', '7:14', '7:19', '7:21', '7:22', '7:25', '7:26', '7:28', '7:35', '7:37', '7:38', '7:41', '7:42', '7:44', '7:49', '7:50', '7:52', '7:56', '8:31', '8:47', '8:55', '8:59', '9:15', '9:23', '9:27', '9:29', '9:30', '9:39', '9:43', '9:45', '9:46', '9:51', '9:53', '9:54', '9:57', '9:58', '10:15', '10:23', '10:27', '10:29', '10:30', '10:39', '10:43', '10:45', '10:46', '10:51', '10:53', '10:54', '10:57', '10:58', '11:07', '11:11', '11:13', '11:14', '11:19', '11:21', '11:22', '11:25', '11:26', '11:28', '11:35', '11:37', '11:38', '11:41', '11:42', '11:44', '11:49', '11:50', '11:52', '11:56'],
             7: ['3:31', '3:47', '3:55', '3:59', '5:31', '5:47', '5:55', '5:59', '6:31', '6:47', '6:55', '6:59', '7:15', '7:23', '7:27', '7:29', '7:30', '7:39', '7:43', '7:45', '7:46', '7:51', '7:53', '7:54', '7:57', '7:58', '9:31', '9:47', '9:55', '9:59', '10:31', '10:47', '10:55', '10:59', '11:15', '11:23', '11:27', '11:29', '11:30', '11:39', '11:43', '11:45', '11:46', '11:51', '11:53', '11:54', '11:57', '11:58'],
             8: ['7:31', '7:47', '7:55', '7:59', '11:31', '11:47', '11:55', '11:59'],
             9: [],
             10: []}
        return d[n]


# APPROACH:  Brute Force
#
# This approach does things a bit backwards; it generates all possible hour and minute times, then checks if the number
# of leds used to represent the generated time is equal to the specified number of illuminated leds.  If they are equal
# then the time is added to a result list.
#
# Time Complexity: O(1), there will always be is 12 * 59 (or a constant number of) iterations.
# Space Complexity: O(1), there are a finite number of valid time combinations (the most is 190 if 5 LEDs are lit).
def binary_watch_time_via_bf(n):
    if isinstance(n, int) and 0 <= n <= 10:
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == n]


# APPROACH: Via Itertools Combinations
#
# This uses the itertools combinations method to generate all possible led combinations, then uses a lookup table to
# sum the values of the illuminated leds using a look-up table of the leds values.
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def binary_watch_time_via_combinations(n):
    if isinstance(n, int) and 0 <= n <= 10:
        leds = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        result = []
        for comb in itertools.combinations(range(len(leds)), n):
            h = sum(leds[i] for i in comb if i < 4)
            m = sum(leds[i] for i in comb if i >= 4)
            if h <= 11 and m <= 59:
                result.append("{}:{:02d}".format(h, m))
        return result


# APPROACH: Via DFS Recursion/Backtracking and Bit Shifting
#
# This is a DFS recursive, or backtracking, solution that uses bit shifting to sum the hour and minute totals.
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def binary_watch_time_via_rec_bit_shift(n):

    def _rec(n, i, h, m):
        if h < 12 and m < 60:
            if n == 0:
                result.append("{}:{:02}".format(h, m))
            else:
                for j in range(i, 10):
                    if j < 4:
                        _rec(n-1, j+1, h|(1<<j), m)
                    else:
                        _rec(n-1, j+1, h, m|(1<<(j-4)))

    if isinstance(n, int) and 0 <= n <= 10:
        result = []
        _rec(n, 0, 0, 0)
        return result


# APPROACH: Via DFS Recursion/Backtracking
#
# This is a DFS recursive, or backtracking, solution that uses powers of two to sum the hour and minute totals.
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def binary_watch_time_via_rec(n):

    def _rec(n, i, h, m):
        if h < 12 and m < 60:
            if n == 0:
                result.append(f"{h}:{m:{0}{2}}")
            else:
                for j in range(i, 10):
                    if j < 6:
                        _rec(n-1, j+1, h, m+(2**j))
                    else:
                        _rec(n-1, j+1, h+(2**(j-6)), m)

    if n is not None and isinstance(n, int) and 0 <= n <= 10:
        result = []
        _rec(n, 0, 0, 0)
        return result


args = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None]
fns = [binary_watch_time_via_lookup_table,
       binary_watch_time_via_bf,
       binary_watch_time_via_combinations,
       binary_watch_time_via_rec_bit_shift,
       binary_watch_time_via_rec]

for n in args:
    for fn in fns:
        print(f"{fn.__name__}({n}): {fn(n)}")
    print()


n = 5   # n = 5 has the longest result list.
for fn in fns:
    print(f"{fn.__name__}() took ", end='')
    t = time.time()
    fn(n)
    print(f"{time.time() - t} seconds.")


