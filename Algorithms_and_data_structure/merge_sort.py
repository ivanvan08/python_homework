"""
# https://www.geeksforgeeks.org/python-program-for-merge-sort/ (by Mohit Kumra)
"""


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


def merge_sort(arr, lo, hi):
    """
    :param arr: array we need to sort
    :param lo: (low) the left index
    :param hi: (high) the right index
    :return: 
    """
    if lo < hi:
        # Same as (l_ind + r_ind) // 2, but avoids overflow for large l_ind and r_ind
        mid = lo + (hi - lo) // 2

        # Sort first and second halves
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid + 1, hi)
        merge(arr, lo, mid, hi)


if __name__ == '__main__':
    data = [12, 11, 13, 5, 6, 7]
    print('Given array is')
    print(data)

    print('\n\n')

    n = len(data)
    merge_sort(data, 0, n - 1)
    print('Sorted array is')
    print(data)

