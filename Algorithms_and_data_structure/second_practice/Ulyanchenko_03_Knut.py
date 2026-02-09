import random
import time


def sorted_elements(size):
    return list(range(size))


def knut(arr):
    for i in range(size - 1, 0, -1):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]
    return arr


def simple_shuffling(arr):
    pair = [(random.random(), el) for el in arr]
    pair.sort()
    return [el[1] for el in pair]


if __name__ == "__main__":
    size = 100
    start = time.time()
    knut = knut(sorted_elements(size))
    print("час після кнута", time.time() - start)
    print("кнут", knut)
    start = time.time()
    simple = simple_shuffling(sorted_elements(size))
    print("час після простого", time.time() - start)
    print("просте", simple)
