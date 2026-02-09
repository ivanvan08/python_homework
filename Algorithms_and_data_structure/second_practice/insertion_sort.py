def insertion_sort(array, lo, hi):
    for step in range(lo + 1, hi + 1):
        key = array[step]
        j = step - 1

        while j >= lo and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key


if __name__ == '__main__':
    data = [9, 5, 1, 4, 3]
    insertion_sort(data, 0, len(data) + 1)
    print('Sorted Array in Ascending Order:')
    print(data)
