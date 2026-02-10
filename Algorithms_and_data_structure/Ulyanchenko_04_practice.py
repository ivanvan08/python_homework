def untersection(arr1, arr2):
    union = []
    intersection = []
    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        elif arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            union.append(arr1[i])
            union.append(arr2[j])
            i += 1
            j += 1
    union += arr1[i:]
    union += arr2[j:]
    return union, intersection


if __name__ == '__main__':
    arr1 = [2, 3, 5, 6]
    arr2 = [1, 3, 4, 5, 7]
    union_result, intersection_result = untersection(arr1, arr2)
    print(f"Input: {arr1}\n{arr2}")
    print(f"Union: {union_result}\nIntersection: {intersection_result}")
