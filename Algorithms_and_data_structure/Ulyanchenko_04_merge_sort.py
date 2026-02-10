"""
# https://www.geeksforgeeks.org/python-program-for-merge-sort/ (by Mohit Kumra)

# не можу надіслати більше 1 файлу на дістеду, тому залишаю посилання на свій гітхаб (завантажте всью папку)
# https://github.com/ivanvan08/python_homework/tree/master/Algorithms_and_data_structure/second_practice
"""
import time

from second_practice.insertion_sort import insertion_sort
from second_practice.Ulyanchenko_03_Knut import sorted_elements, simple_shuffling
from second_practice.practice_2 import partly_sorted_elements


def merge(arr, lo, mid, hi):
    """
    :param arr: array we need to merge
    :param lo: (low) the index of the first subarray beginning
    :param mid: middle index
    :param hi: (high) the index of the second subarray ending
    :return:
    """

    # create temp arrays and copy data to them
    left = arr[lo:(mid + 1)]
    right = arr[(mid + 1):(hi + 1)]

    left_count = len(left)
    right_count = len(right)

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray (left)
    j = 0  # Initial index of second subarray (right)
    k = lo  # Initial index of merged subarray

    while i < left_count and j < right_count:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of first subarray, if there are any
    while i < left_count:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of second subarray, if there are any
    while j < right_count:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort_standard(arr, lo, hi):
    if lo < hi:
        mid = lo + (hi - lo) // 2
        merge_sort_standard(arr, lo, mid)
        merge_sort_standard(arr, mid + 1, hi)
        merge(arr, lo, mid, hi)


def merge_sort(arr, lo, hi):
    """
    :param arr: array we need to sort
    :param lo: (low) the left index
    :param hi: (high) the right index
    :return: 
    """
    if lo < hi:
        if hi - lo + 1 <= 7:  # +1 in case of index
            insertion_sort(arr, lo, hi)
            return
        # Same as (l_ind + r_ind) // 2, but avoids overflow for large l_ind and r_ind
        mid = lo + (hi - lo) // 2

        # Sort first and second halves
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid + 1, hi)
        if arr[mid] <= arr[mid + 1]:
            return
        merge(arr, lo, mid, hi)


if __name__ == '__main__':
    size_for_merge = 1000
    size_for_insertion = 7
    sorted_merge = sorted_elements(size_for_merge)
    sorted_insertion = sorted_elements(size_for_insertion)
    shuffled_merge = simple_shuffling(sorted_elements(size_for_merge))
    shuffled_insertion = simple_shuffling(sorted_elements(size_for_insertion))
    partly_sorted_merge = partly_sorted_elements(size_for_merge)
    partly_sorted_insertion = partly_sorted_elements(size_for_insertion)

    # при оцінці часу сортування зважайте на "e-" в кінці, будь ласка

    start = time.time()
    merge_sort(sorted_merge, 0, size_for_merge - 1)
    print(f"sorted 1000 elements: {time.time() - start}")

    start = time.time()
    merge_sort(sorted_insertion, 0, size_for_insertion - 1)
    print(f"sorted 7 elements: {time.time() - start}")

    start = time.time()
    merge_sort(shuffled_merge, 0, size_for_merge - 1)
    print(f"shuffled 1000 elements: {time.time() - start}")

    start = time.time()
    merge_sort(shuffled_insertion, 0, size_for_insertion - 1)
    print(f"shuffled 7 elements: {time.time() - start}")

    start = time.time()
    merge_sort(partly_sorted_merge, 0, size_for_merge - 1)
    print(f"partly shuffled 1000 elements: {time.time() - start}")

    start = time.time()
    merge_sort(partly_sorted_insertion, 0, size_for_insertion - 1)
    print(f"partly shuffled 7 elements: {time.time() - start}\n")
    print(f"Standard merge\n")

    sorted_merge = sorted_elements(size_for_merge)
    sorted_insertion = sorted_elements(size_for_insertion)
    shuffled_merge = simple_shuffling(sorted_elements(size_for_merge))
    shuffled_insertion = simple_shuffling(sorted_elements(size_for_insertion))
    partly_sorted_merge = partly_sorted_elements(size_for_merge)
    partly_sorted_insertion = partly_sorted_elements(size_for_insertion)

    start = time.time()
    merge_sort_standard(sorted_merge, 0, size_for_merge - 1)
    print(f"standard sorted 1000 elements: {time.time() - start}")

    start = time.time()
    merge_sort_standard(sorted_insertion, 0, size_for_insertion - 1)
    print(f"standard sorted 7 elements: {time.time() - start}")

    start = time.time()
    merge_sort_standard(shuffled_merge, 0, size_for_merge - 1)
    print(f"standard shuffled 1000 elements: {time.time() - start}")

    start = time.time()
    merge_sort_standard(shuffled_insertion, 0, size_for_insertion - 1)
    print(f"standard shuffled 7 elements: {time.time() - start}")

    start = time.time()
    merge_sort_standard(partly_sorted_merge, 0, size_for_merge - 1)
    print(f"standard partly shuffled 1000 elements: {time.time() - start}")

    start = time.time()
    merge_sort_standard(partly_sorted_insertion, 0, size_for_insertion - 1)
    print(f"standard partly shuffled 7 elements: {time.time() - start}")
