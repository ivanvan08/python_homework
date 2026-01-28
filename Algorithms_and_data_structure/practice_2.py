import random
from Algorithms_and_data_structure.SelectionSort import selection_sort
from Algorithms_and_data_structure.InsertionSort import insertion_sort

import time


# from pyparsing import delimited_list


# def random_elements(size):
#     return random.randrange(size)


def random_elements(size):
    el_list = list(range(size))
    for i in range(size - 1, 0, -1):
        r = random.randint(0, i)
        el_list[i], el_list[r] = el_list[r], el_list[i]
    return el_list


def sorted_elements(size):
    return list(range(size))


def partly_sorted_elements(size):
    first_el = int(size * 0.9)
    second_el = size - first_el
    return sorted_elements(first_el) + random_elements(second_el)


def test_selection_sort(size):
    start = time.time()
    selection_sort(random_elements(size))
    print(time.time() - start)

    start = time.time()
    selection_sort(sorted_elements(size))
    print(time.time() - start)

    start = time.time()
    selection_sort(partly_sorted_elements(size))
    print(time.time() - start)


def test_insertion_sort(size):
    start = time.time()
    insertion_sort(random_elements(size))
    print(time.time() - start)

    start = time.time()
    insertion_sort(sorted_elements(size))
    print(time.time() - start)

    start = time.time()
    insertion_sort(partly_sorted_elements(size))
    print(time.time() - start)


if __name__ == "__main__":
    size = 20000
    test_insertion_sort(size)
