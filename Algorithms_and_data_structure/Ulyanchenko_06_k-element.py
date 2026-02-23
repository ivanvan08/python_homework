"""
To achieve same results on shuffled and ordered lists I used knut to shuffle arr previously. Yes, it will take some
resources, but it's good easy way to do this, as in previous home task
"""

import random


def knut(arr):
    for i in range(len(arr) - 1, 0, -1):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]
    return arr


def k_largest(arr, k):
    arr = knut(arr)
    target_index = len(arr) - k
    lo = 0
    hi = len(arr)
    while lo <= hi:
        limit = lo
        pivot = arr[lo]
        for i in range(lo + 1, hi):
            if arr[i] < pivot:
                limit += 1
                arr[i], arr[limit] = arr[limit], arr[i]
        arr[lo], arr[limit] = arr[limit], arr[lo]
        if limit == target_index:
            return arr[target_index]
        elif limit < target_index:
            lo = limit + 1
        elif limit > target_index:
            hi = limit


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(k_largest(nums, k))
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(k_largest(nums, k))
