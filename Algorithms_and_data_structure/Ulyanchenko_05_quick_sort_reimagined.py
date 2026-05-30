from second_practice.insertion_sort import insertion_sort


def quick_sort(arr, lo, hi):
    if hi < lo+15:
        insertion_sort(arr, lo, hi)
    else:
        mid = lo + (hi - lo) // 2

