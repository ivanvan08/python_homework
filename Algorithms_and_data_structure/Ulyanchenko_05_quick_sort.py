import time
from second_practice.practice_2 import random_elements, partly_sorted_elements, \
    sorted_elements, insertion_sort


def quick_sort(arr, lo, hi):
    if hi <= lo + 9:  # upgrade 1
        insertion_sort(arr, lo, hi)
    else:
        mid = lo + (hi - lo) // 2

        if arr[mid] < arr[lo]:
            arr[lo], arr[mid] = arr[mid], arr[lo]
        if arr[hi] < arr[lo]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[hi] < arr[mid]:
            arr[mid], arr[hi] = arr[hi], arr[mid]
        arr[lo], arr[mid] = arr[mid], arr[lo]

        i = lo + 1
        j = hi
        while i < j:
            while arr[i] < arr[lo]:
                i += 1
            while arr[j] > arr[lo]:
                j -= 1
            if i >= j:  # if smth will go wrong
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        arr[lo], arr[j] = arr[j], arr[lo]
        quick_sort(arr, lo, j - 1)
        quick_sort(arr, j + 1, hi)


if __name__ == '__main__':
    size_q = 1000
    size_ins = 7

    sorted_q = sorted_elements(size_q)
    sorted_ins = sorted_elements(size_ins)

    shuffled_q = random_elements(size_q)
    shuffled_ins = random_elements(size_ins)

    partly_sorted_q = partly_sorted_elements(size_q)
    partly_sorted_ins = partly_sorted_elements(size_ins)

    start = time.time()
    quick_sort(sorted_q, 0, size_q - 1)
    print(f"Sorted 1000 elements: {time.time() - start:.10f}")

    start = time.time()
    quick_sort(sorted_ins, 0, size_ins - 1)
    print(f"Sorted 7 elements: {time.time() - start:.10f}")

    start = time.time()
    quick_sort(shuffled_q, 0, size_q - 1)
    print(f"Shuffled 1000 elements: {time.time() - start:.10f}")

    start = time.time()
    quick_sort(shuffled_ins, 0, size_ins - 1)
    print(f"Shuffled 7 elements: {time.time() - start:.10f}")

    start = time.time()
    quick_sort(partly_sorted_q, 0, size_q - 1)
    print(f"Partly shuffled 1000 elements: {time.time() - start:.10f}")

    start = time.time()
    quick_sort(partly_sorted_ins, 0, size_ins - 1)
    print(f"Partly shuffled 7 elements: {time.time() - start:.10f}")
