"""
    CONTINUOUS MEDIAN

    Numbers are randomly generated and passed to a method.  Write a program to find and maintain the median value as new
    values are generated.

    Remember, to find the median of a group of numbers:
        1.  Arrange the numbers in order by size.
        2.  If there is an odd number of terms, the median is the center term.
        3.  If there is an even number of terms, add the two middle terms and divide by 2.
"""
import heapq
import random


class ContinuousMedian:
    def __init__(self):
        self.max_heap = list()
        self.min_heap = list()

    def add_new_number(self, num):
        if len(self.max_heap) == len(self.min_heap):
            if self.min_heap is not None and len(self.min_heap) > 0 and num > self.min_heap[0]:
                self.max_heap.append(heapq.heappop(self.min_heap))
                heapq._siftdown_max(self.max_heap, 0, len(self.max_heap) - 1)
                heapq.heappush(self.min_heap, num)
            else:
                self.max_heap.append(num)
                heapq._siftdown_max(self.max_heap, 0, len(self.max_heap) - 1)
        else:
            if num < self.max_heap[0]:
                heapq.heappush(self.min_heap, heapq._heappop_max(self.max_heap))
                self.max_heap.append(num)
                heapq._siftdown_max(self.max_heap, 0, len(self.max_heap) - 1)
            else:
                heapq.heappush(self.min_heap, num)

    def get_median(self):
        if len(self.max_heap) == 0:
            return None
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + self.max_heap[0]) / 2
        return self.max_heap[0]  # If max_heap and min_heap are different sizes, max_heap has one more


continuous_median = ContinuousMedian()
for _ in range(10):
    random_num = random.randint(0, 1000)
    print("random_num:", random_num)
    print("continuous_median.add_new_number(random_num)"); continuous_median.add_new_number(random_num)
    print("continuous_median.min_heap:", continuous_median.min_heap)
    print("continuous_median.max_heap:", continuous_median.max_heap)
    print("continuous_median.get_median():", continuous_median.get_median())
    print()














