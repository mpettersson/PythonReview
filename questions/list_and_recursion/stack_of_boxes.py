"""
    STACK OF BOXES (CCI 8.13)

    You have a stack of n boxes, with widths wi, heights hi, and depths di.  The boxes cannot be rotated and can only be
    stacked on top of one another if each box in the stack is strictly larger than the box above it in width, height,
    and depth.  Implement a method to compute the height of the tallest possible stack.  The height of a stack is the
    sum of the heights of each box.
"""


def stack_of_boxes(boxes):

    def _stack_of_boxes(boxes, bottom_index):
        bottom = boxes[bottom_index]
        max_h = 0
        for i in range(bottom_index + 1, len(boxes)):
            if boxes[i].can_be_above(bottom):
                max_h = max(max_h, _stack_of_boxes(boxes, i))
        return max_h + bottom.h

    if boxes is not None:
        max_h = 0
        boxes.sort(key=lambda x: x.h, reverse=True)
        for i in range(len(boxes)):
            max_h = max(max_h, _stack_of_boxes(boxes, i))
        return max_h


def stack_of_boxes_memo(boxes):

    def _stack_of_boxes_memo(boxes, bottom_index, memo):
        if bottom_index < len(boxes) and memo[bottom_index] > 0:
            return memo[bottom_index]

        bottom = boxes[bottom_index]
        max_h = 0
        for i in range(bottom_index + 1, len(boxes)):
            if boxes[i].can_be_above(bottom):
                max_h = max(max_h, _stack_of_boxes_memo(boxes, i, memo))
        max_h += bottom.h
        memo[bottom_index] = max_h
        return max_h

    if boxes is not None:
        max_h = 0
        boxes.sort(key=lambda x: x.h, reverse=True)
        memo = [0] * len(boxes)
        for i in range(len(boxes)):
            max_h = max(max_h, _stack_of_boxes_memo(boxes, i, memo))
        return max_h


def stack_of_boxes_memo_alt(boxes):

    def _stack_of_boxes_memo_alt(boxes, bottom, offset, memo):
        if offset >= len(boxes):
            return 0

        # height with this bottom:
        new_bottom = boxes[offset]
        height_w_bottom = 0
        if bottom is None or new_bottom.can_be_above(bottom):
            if memo[offset] is 0:
                memo[offset] = _stack_of_boxes_memo_alt(boxes, new_bottom, offset + 1, memo)
                memo[offset] += new_bottom.h
            height_w_bottom = memo[offset]

        # Without this bottom:
        height_wo_bottom = _stack_of_boxes_memo_alt(boxes, bottom, offset + 1, memo)
        return max(height_w_bottom, height_wo_bottom)

    if boxes is not None:
        boxes.sort(key=lambda x: x.h, reverse=True)
        memo = [0] * len(boxes)
        return _stack_of_boxes_memo_alt(boxes, None, 0, memo)


class box:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def __repr__(self):
        return f"{self.w}x{self.h}x{self.d}"

    def can_be_above(self, b):
        if b is not None and self.w < b.w and self.h < b.h and self.d < b.w:
            return True
        return False


import random

# boxes = [box(6, 6, 8), box(6, 4, 11), box(6, 3, 5), box(4, 2, 12), box(9, 11, 11), box(12, 3, 5), box(10, 3, 9), box(11, 5, 6), box(7, 17, 14), box(6, 6, 2)]

boxes = []
boxes.extend([box(random.randint(1, 10+i), random.randint(1, 10+i), random.randint(1, 10+i)) for i in range(10)])

print(boxes)

print(stack_of_boxes(boxes))
print(stack_of_boxes_memo(boxes))
print(stack_of_boxes_memo_alt(boxes))

