def selection_sort(array):
    for i in range(len(array)):
        min_indx = i
        for j in range(i + 1, len(array)):
            if array[min_indx] > array[j]:
                min_indx = j
        array[i], array[min_indx] = array[min_indx], array[i]
    return array


if __name__ == '__main__':
    data = [5, 6, 4, 2]
    selection_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
